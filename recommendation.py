import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

purchase_data = pd.read_csv('customer_purchases.csv')
customer_segments = pd.read_csv('customer_segments.csv')

# Merge purchase data with customer segments
df = purchase_data.merge(customer_segments[['Customer ID', 'Segment']], on='Customer ID')

# Create a pivot table: customers vs. products (purchase counts)
user_product_matrix = df.pivot_table(
    index='Customer ID',
    columns='Product ID',
    values='Purchase Amount',
    aggfunc='count',
    fill_value=0
)

# Initialize the model
model = NearestNeighbors(metric='cosine', n_neighbors=5)
model.fit(user_product_matrix)

# Function to get recommendations
def recommend_products(customer_id, n_recommendations=5):
    # Find nearest neighbors
    distances, indices = model.kneighbors(
        [user_product_matrix.loc[customer_id]], 
        n_neighbors=5
    )
    
    # Get neighbor customer IDs
    neighbor_ids = user_product_matrix.index[indices[0]]
    
    # Aggregate products bought by neighbors
    neighbor_purchases = user_product_matrix.loc[neighbor_ids].sum(axis=0)
    
    # Filter out products already bought by the target customer
    target_purchases = user_product_matrix.loc[customer_id]
    recommendations = neighbor_purchases[target_purchases == 0]
    
    # Sort by popularity and return top N
    return recommendations.sort_values(ascending=False).head(n_recommendations).index.tolist()

# Example: Recommend products for customer "C123"
customer_id = "C123"
recommended_products = recommend_products(customer_id)

print(f"\nRecommended products for {customer_id}:")
print(recommended_products)

def segment_enhanced_recommendations(customer_id, n_recommendations=5):
    # Get the customer's segment (e.g., "High Spenders")
    segment = customer_segments.loc[
        customer_segments['Customer ID'] == customer_id, 'Segment'
    ].values[0]
    
    # Get popular products in the segment
    segment_customers = customer_segments[customer_segments['Segment'] == segment]['Customer ID']
    segment_purchases = df[df['Customer ID'].isin(segment_customers)]
    top_segment_products = segment_purchases['Product ID'].value_counts().head(10).index.tolist()
    
    # Filter out products the customer already bought
    target_purchases = df[df['Customer ID'] == customer_id]['Product ID'].tolist()
    recommendations = [p for p in top_segment_products if p not in target_purchases]
    
    return recommendations[:n_recommendations]