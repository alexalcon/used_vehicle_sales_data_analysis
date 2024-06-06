# Objective Analysis 1: Profit Margin Analysis

## Overview

This analysis focuses on calculating the profit margins for various used vehicles. The goal is to determine which brands and models are the most profitable. The results are saved in both CSV format and as visual plots for easy interpretation.

## Directory Structure

```
objective_analysis_1
├── data
│ └── profit_by_brand_model.csv
├── results
│ ├── profit_by_brand_and_model_table.png
│ └── profit_margin_by_brand_and_model_bar_chart.png
├── scripts
│ ├── profit_and_profit_margin_table.py
│ └── profit_and_profit_margin.py
└── README.md
```

## Files Description

- **data/profit_by_brand_model.csv**: Contains the profit and profit margin calculations for each brand and model.
- **results/profit_by_brand_and_model_table.png**: Image of the table summarizing profit and profit margin by brand and model.
- **results/profit_margin_by_brand_and_model_bar_chart.png**: Bar chart visualizing the profit margin for each brand and model.
- **scripts/profit_and_profit_margin_table.py**: Python script to generate and save the table of profit margins.
- **scripts/profit_and_profit_margin.py**: Python script to calculate profit and profit margin, and to generate the bar chart.
- **README.md**: This README file explaining the directory structure and contents.

## Analysis Methodology

1. **Data Loading**:
   - The dataset is loaded with appropriate encoding and delimiter settings.

2. **Data Cleaning**:
   - The relevant columns `Precio Compra` and `Precio Venta` are converted to numeric values.
   - Rows with missing values in these critical columns are dropped.

3. **Profit Calculation**:
   - Profit for each vehicle is calculated using equation 1 described in the report file.

4. **Profit Margin Calculation**:
   - Profit for each vehicle is calculated using equation 2 described in the report file.

5. **Aggregation**:
   - The data is grouped by brand and model to calculate the mean profit and profit margin.

6. **Results**:
   - The results are saved in a CSV file and visualized using a bar chart.
   - A vertical line indicating the average profit margin is included in the bar chart for reference.

## How to Run the Scripts

### Prerequisites

- Python 3.12.0
- Pandas
- Matplotlib

Just create a venv directory.

### Running the Profit and Profit Margin Calculation

1. Navigate to the `scripts` directory.
2. Run the `profit_and_profit_margin.py` script:
   ```sh
   python profit_and_profit_margin.py
   