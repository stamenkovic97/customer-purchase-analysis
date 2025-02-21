import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('customer_purchases.csv')

# Top 10 products
top_products = df['Product ID'].value_counts().head(10)

# Top 5 categories
top_categories = df['Category'].value_counts().head(5)

# Visualize the results
plt.figure(figsize=(10, 6))

# Plot top products
plt.subplot(1, 2, 1)
top_products.plot(kind='bar', color='skyblue')
plt.title('Top 10 Products')
plt.xlabel('Product ID')
plt.ylabel('Number of Purchases')

# Plot top categories
plt.subplot(1, 2, 2)
top_categories.plot(kind='bar', color='lightgreen')
plt.title('Top 5 Categories')
plt.xlabel('Category')
plt.ylabel('Number of Purchases')

plt.tight_layout()
plt.savefig('sales_analysis.png')
plt.show()

# Average spending per customer
avg_spending = df.groupby('Customer ID')['Purchase Amount'].mean().reset_index()
avg_spending.columns = ['Customer ID', 'Average Spending']

# Visualize distribution
plt.figure(figsize=(8, 5))
plt.hist(avg_spending['Average Spending'], bins=20, color='purple', edgecolor='black')
plt.title('Distribution of Average Spending per Customer')
plt.xlabel('Average Spending ($)')
plt.ylabel('Number of Customers')
plt.savefig('avg_spending_distribution.png')
plt.show()