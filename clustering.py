import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv('customer_purchases.csv')

# Aggregate customer-level features
customer_features = df.groupby('Customer ID').agg({
    'Purchase Amount': ['sum', 'mean', 'count'],
    'Category': 'nunique'
}).reset_index()

# Rename columns for clarity
customer_features.columns = [
    'Customer ID',
    'Total Spent',
    'Average Spending',
    'Purchase Count',
    'Unique Categories'
]

# Select features for clustering
X = customer_features[['Total Spent', 'Purchase Count', 'Average Spending']]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Calculate inertia for k=1 to k=10
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o', linestyle='--')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.savefig('elbow_plot.png')
plt.show()

# Fit K-means with k=3
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Add clusters to customer_features
customer_features['Cluster'] = clusters

# Assign segment labels
cluster_labels = {
    0: 'Occasional Shoppers',
    1: 'High Spenders',
    2: 'Frequent Buyers'
}
customer_features['Segment'] = customer_features['Cluster'].map(cluster_labels)

# Calculate cluster means (exclude non-numeric columns)
numeric_features = customer_features.drop(columns=['Customer ID', 'Segment'])
cluster_means = numeric_features.groupby('Cluster').mean()

# Reduce to 2D using PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plot clusters
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis', alpha=0.6)
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('Customer Segments (PCA Visualization)')
plt.legend(handles=scatter.legend_elements()[0], labels=cluster_labels.values())
plt.savefig('customer_segments.png')
plt.show()

customer_features.to_csv('customer_segments.csv', index=False)