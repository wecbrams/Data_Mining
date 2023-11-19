---

# Market Basket Analysis with Apriori Algorithm

## Overview

This project performs Market Basket Analysis on grocery store data using the Apriori algorithm. Market Basket Analysis helps identify relationships between products, enabling businesses to make informed decisions about product placement, promotions, and customer preferences.

## Table of Contents

- [Dataset](#dataset)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Files](#files)
- [License](#license)

## Dataset

The dataset used for this analysis is "Market_Basket_Optimisation.csv," which contains transactional data from a grocery store. Each row represents a transaction, and the columns contain the purchased items.

## Prerequisites

Before running the code, make sure you have the following installed:

- Python 3
- Required libraries: numpy, pandas, matplotlib, mlxtend

You can install the required libraries using:

```bash
pip install numpy pandas matplotlib mlxtend
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/market-basket-analysis.git
cd market-basket-analysis
```

2. Run the Jupyter Notebook or Python script.

## Usage

Execute the Jupyter Notebook or Python script to perform the Market Basket Analysis. The analysis includes:

- Data preprocessing
- One-hot encoding
- Applying the Apriori algorithm
- Extracting association rules based on confidence and support
- Creating scatter plots of confidence vs. support and lift vs. support
- Saving the results to Excel files

## Results

The results of the analysis are saved in the following files:

- Generated_Rules_conf.xlsx: Association rules based on confidence
- Generated_Rules_supp.xlsx: Association rules based on support
- Best_Confidence_Rules.xlsx: Top confidence-based association rules
- Best_Support_Rules.xlsx: Top support-based association rules
- Recommendations.xlsx: Product recommendations based on the best rules

Scatter plots are saved as Support_vs_Confidence.png and Support_vs_Lift.png.

## Files

- `Market_Basket_Optimisation.csv`: Input dataset
- `market_basket_analysis.ipynb`: Jupyter Notebook for the analysis
- `market_basket_analysis.py`: Python script for the analysis
- `Generated_Rules_conf.xlsx`, `Generated_Rules_supp.xlsx`, `Best_Confidence_Rules.xlsx`, `Best_Support_Rules.xlsx`, `Recommendations.xlsx`: Output files
- `Support_vs_Confidence.png`, `Support_vs_Lift.png`: Scatter plots

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
