import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Step 1: Generate product data
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Beauty', 'Sports']
products = pd.DataFrame({
    'Product ID': [f'P{i}' for i in range(1, 51)],
    'Category': np.random.choice(categories, size=50)
})

# Step 2: Generate purchase records
purchase_data = pd.DataFrame({
    'Customer ID': np.random.choice([f'C{i}' for i in range(1, 501)], size=5000),
    'Product ID': np.random.choice(products['Product ID'], size=5000),
    'Purchase Amount': np.round(np.random.uniform(10, 500, size=5000), 2),
    'Purchase Date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(5000)]
})

# Step 3: Merge with product categories
purchase_data = purchase_data.merge(products, on='Product ID')

# Step 4: Save to CSV
purchase_data.to_csv('customer_purchases.csv', index=False)

# Load and verify
df = pd.read_csv('customer_purchases.csv')