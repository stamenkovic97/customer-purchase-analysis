# Customer Purchase Analysis

![Python Version](https://img.shields.io/badge/python-3.13.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A retail customer segmentation and recommendation system using clustering and AI.

## Features
- Synthetic dataset generation
- Customer spending analysis
- K-means clustering for segmentation
- Product recommendation engine

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/stamenkovic97/customer-purchase-analysis.git
   cd customer-purchase-analysis
   ```

2. Install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Generate synthetic data:
   ```bash
   python3 generate_data.py
   ```

4. Run analysis:
   ```bash
   python3 analyze_data.py
   ```

## Project Structure
```
.
├── generate_data.py       # Synthetic data generation
├── analyze_data.py        # Data analysis and visualization
├── README.md              # Project documentation
└── requirements.txt       # Dependency list
```

## License
MIT License - See [LICENSE](LICENSE) for details.