# Data Analysis Report: Used Vehicle Sales

## Overview

This repository contains the code and analysis for evaluating a dataset related to the purchase and sale of used vehicles. The analysis includes calculating profit margins, evaluating inventory times, assessing market demand, and understanding buyer profiles. The goal is to derive actionable insights to aid in business decision-making.

## Repository Structure

The repository is structured into several directories, each corresponding to a specific objective of the analysis:

```
.
├── objective_analysis_1
│ ├── data
│ │ └── profit_by_brand_model.csv
│ ├── results
│ │ ├── profit_margin_by_brand_and_model_bar_chart.png
│ │ └── profit_by_brand_and_model_table.png
│ ├── scripts
│ │ ├── profit_and_profit_margin.py
│ │ └── profit_and_profit_margin_table.py
│ └── README.md
├── objective_analysis_2
│ ├── data
│ │ └── inventory_time_by_brand_model.csv
│ ├── results
│ │ ├── inventory_time_by_brand_and_model_bar_chart.png
│ │ └── inventory_time_by_brand_and_model_table.png
│ ├── scripts
│ │ ├── inventory_time_analysis.py
│ │ └── create_inventory_time_table.py
│ └── README.md
├── report.pdf
├── reporte.pdf
└── README.md
```
## Objectives and Methodologies

### Objective 1: Profit Margin Analysis
**Goal**: Calculate the average profit margin for each vehicle.

**Methodology**:
1. Calculate the profit for each transaction by subtracting the purchase price from the sale price.
2. Calculate the profit margin for each transaction.
3. Calculate the average profit margin across all transactions.
4. Identify brands and models with the highest profit margins.

### Objective 2: Inventory Time Analysis
**Goal**: Determine which vehicles have the shortest and longest average inventory times.

**Methodology**:
1. Calculate the average inventory time for each brand and model.
2. Identify which vehicles sell the fastest and which take the longest to sell.

## Usage

### Setting Up the Virtual Environment

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/used-vehicle-sales-analysis.git
    ```

2. Create a Python virtual environment with the following Prerequisites: 

    - Python 3.12.0
    - Pandas
    - Matplotlib