# Objective Analysis 2: Inventory Time Analysis

## Overview

This analysis focuses on calculating the average inventory time for various used vehicles. The goal is to determine which brands and models sell the fastest and which take the longest to sell.

## Directory Structure

```
objective_analysis_2/
├── data/
│   └── inventory_time_by_brand_model.csv
├── results/
│   ├── inventory_time_by_brand_and_model_table.png
│   └── inventory_time_by_brand_and_model_bar_chart.png
├── scripts/
│   └── inventory_time_analysis.py
│   └── inventory_time_analysis_table.py
└── README.md
```

## Files Description

- **data/inventory_time_by_brand_model.csv**: Contains the average inventory time calculations for each brand and model.
- **results/inventory_time_by_brand_and_model_table.png**: Image of the table summarizing average inventory time by brand and model.
- **results/inventory_time_by_brand_and_model_bar_chart.png**: Bar chart visualizing the average inventory time for each brand and model.
- **scripts/inventory_time_analysis.py**: Python script to calculate average inventory time and generate the bar chart.
- **scripts/inventory_time_analysis_table.py**: Python script to generate the average inventory time table.
- **README.md**: This README file explaining the directory structure and contents.

## Analysis Methodology

1. **Data Loading**:
   - The dataset is loaded with appropriate encoding and delimiter settings.

2. **Data Cleaning**:
   - The relevant column `Tiempo en Inventario (días)` is converted to numeric values.
   - Rows with missing values in this critical column are dropped.

3. **Average Inventory Time Calculation**:
   - The average inventory time for each vehicle is calculated using equation 4 described in the report file

4. **Results**:
   - The results are saved in a CSV file and visualized using a bar chart.

## How to Run the Scripts

### Prerequisites

- Python 3.12.0
- Pandas
- Matplotlib

Just create a venv directory.

### Running the Profit and Profit Margin Calculation

1. Navigate to the `scripts` directory.
2. Run the `inventory_time_analysis.py` script:
   ```sh
   python inventory_time_analysis.py
   
