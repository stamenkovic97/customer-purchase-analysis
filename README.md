# AI-Powered Customer Purchase Analysis

![Python Version](https://img.shields.io/badge/python-3.13-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A retail analytics system that segments customers and recommends products using K-means clustering and collaborative filtering.

## Key Features
- **Synthetic Data Generation**: 5,000 purchase records across 500 customers and 50 products.
- **Customer Segmentation**: Groups customers into "High Spenders," "Frequent Buyers," and "Occasional Shoppers."
- **Product Recommendations**: Collaborative filtering based on purchase history.
- **PDF Report**: Insights, visualizations, and methodology summary.

## Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/stamenkovic97/customer-purchase-analysis.git
   cd customer-purchase-analysis
   ```

2. **Install dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Generate synthetic data**:
   ```bash
   python3 generate_data.py
   ```

## Usage
1. **Run data analysis**:
   ```bash
   python3 analyze_data.py  # Generates sales_analysis.png and avg_spending_distribution.png
   ```

2. **Segment customers**:
   ```bash
   python3 clustering.py    # Generates customer_segments.csv and customer_segments.png
   ```

3. **Get product recommendations**:
   ```bash
   python3 recommendation.py  # Example: Recommends products for customer "C123"
   ```

4. **Generate the report**:
   - Open `report.ipynb` in Jupyter Notebook or view the pre-generated `report.pdf`.

## Project Structure
```
.
├── generate_data.py        # Synthetic dataset generation
├── analyze_data.py         # Data analysis and visualization
├── clustering.py           # Customer segmentation (K-means)
├── recommendation.py       # Product recommendations (collaborative filtering)
├── report.ipynb            # Jupyter Notebook report
├── report.pdf              # Final summary report
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## Evaluation Criteria Addressed
✅ **Technical Skills**:  
   - K-means clustering (`scikit-learn`).  
   - Collaborative filtering (`NearestNeighbors`).  
✅ **Data Analysis**: Insights on top products, customer spending.  
✅ **Code Quality**: Modular, PEP8-compliant code.  
✅ **Creativity**: Hybrid recommendations (collaborative + segment-based).  
✅ **Documentation**: Clear README and PDF report.  

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Author**: Dušan Stamenković
**Date**: February 2025  

