import pandas as pd
import matplotlib.pyplot as plt

# load the dataset 
file_path = "../../dataset/dataset.csv"

# try loading with different encodings
# specify encoding and delimiter
try:
    df = pd.read_csv(file_path, encoding='utf-8', delimiter=';')
    print("File loaded successfully with utf-8 encoding and semicolon delimiter.")
except UnicodeDecodeError:
    print("utf-8 encoding failed, trying with latin1 encoding and semicolon delimiter.")
    df = pd.read_csv(file_path, encoding='latin1', delimiter=';')
    print("File loaded successfully with latin1 encoding and semicolon delimiter.")

# ensure required columns are present
required_columns = ['Precio Compra', 'Precio Venta']
for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Error: Missing required column '{column}'. Please check the dataset.")

# convert relevant columns to numeric
df['Precio Compra'] = pd.to_numeric(df['Precio Compra'], errors='coerce')
df['Precio Venta'] = pd.to_numeric(df['Precio Venta'], errors='coerce')

# drop rows with missing values in critical columns
df.dropna(subset=['Precio Compra', 'Precio Venta'], inplace=True)

# calculate profit for each vehicle
# equation 1
df['Profit'] = df['Precio Venta'] - df['Precio Compra']

# calculate profit margin for each vehicle
# equation 2
df['Profit Margin (%)'] = (df['Profit'] / df['Precio Venta']) * 100

# calculate average profit margin
# equation 3
average_profit_margin = df['Profit Margin (%)'].mean()
print(f"Average Profit Margin: {average_profit_margin:.2f}%")

# group by brand and model to see which are most profitable
profit_by_brand_model = df.groupby(['Marca', 'Modelo']).agg({
    'Profit': 'mean',
    'Profit Margin (%)': 'mean'
}).reset_index()

# sort by Profit Margin
profit_by_brand_model = profit_by_brand_model.sort_values(by='Profit Margin (%)', ascending=False)

# save the results to a new CSV file
output_file_path = '../data/profit_by_brand_model.csv'
profit_by_brand_model.to_csv(output_file_path, index=False)

# display the result
print(profit_by_brand_model.head())

# profit margin by vehicle brand and model bar chart
plt.figure(figsize=(12, 8))
plt.barh(profit_by_brand_model['Marca'] + ' ' + profit_by_brand_model['Modelo'], profit_by_brand_model['Profit Margin (%)'])
plt.axvline(average_profit_margin, color='red', linestyle='--', linewidth=1, label=f'Average Profit Margin ({average_profit_margin:.2f}%)')
plt.xlabel('Profit Margin (%)')
plt.ylabel('Brand and Model')
plt.title('Profit Margin by Brand and Model')
plt.legend()
plt.grid(axis='x', linestyle='--', color='gray', linewidth=0.5, alpha=0.7)
plt.gca().invert_yaxis()
plt.show()

