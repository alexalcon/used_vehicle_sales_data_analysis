import pandas as pd
import matplotlib.pyplot as plt

# load the dataset with specified encoding and delimiter
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
required_columns = ['Marca', 'Modelo', 'Tiempo en Inventario (días)']
for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Error: Missing required column '{column}'. Please check the dataset.")

# convert relevant columns to numeric
df['Tiempo en Inventario (días)'] = pd.to_numeric(df['Tiempo en Inventario (días)'], errors='coerce')

# drop rows with missing values in critical columns
df.dropna(subset=['Tiempo en Inventario (días)'], inplace=True)

# calculate average inventory time for each brand and model
# equation 4
inventory_time_by_brand_model = df.groupby(['Marca', 'Modelo']).agg({
    'Tiempo en Inventario (días)': 'mean'
}).reset_index()

# rename columns for clarity
inventory_time_by_brand_model.rename(columns={'Tiempo en Inventario (días)': 'Average Inventory Time (days)'}, inplace=True)

# sort by Average Inventory Time
inventory_time_by_brand_model = inventory_time_by_brand_model.sort_values(by='Average Inventory Time (days)')

# save the results to a new CSV file
output_file_path = '../data/inventory_time_by_brand_model.csv'
inventory_time_by_brand_model.to_csv(output_file_path, index=False)

# display the result
print(inventory_time_by_brand_model.head())

# plot the average inventory time for each brand and model
plt.figure(figsize=(12, 8))
plt.barh(inventory_time_by_brand_model['Marca'] + ' ' + inventory_time_by_brand_model['Modelo'], inventory_time_by_brand_model['Average Inventory Time (days)'])
plt.xlabel('Average Inventory Time (days)')
plt.ylabel('Brand and Model')
plt.title('Average Inventory Time by Brand and Model')
plt.grid(axis='x', linestyle='--', color='gray', linewidth=0.5, alpha=0.7)
plt.gca().invert_yaxis()
plt.show()
