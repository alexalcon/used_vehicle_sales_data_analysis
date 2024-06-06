import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file
data = pd.read_csv('../data/profit_by_brand_model.csv')

# combine 'Marca' and 'Modelo' into a single 'Brand and Model' column
data['Brand and Model'] = data['Marca'] + ' ' + data['Modelo']

# display the data as a table
print("Data Table:")
print(data)

# create a table figure
# profit by vehicle brand and model
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=data.values, colLabels=data.columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
plt.title('Profit by Brand and Model Table')
plt.show()

# calculate the average profit margin
average_profit_margin = data['Profit Margin (%)'].mean()

# sort data by Profit Margin
data_sorted = data.sort_values(by='Profit Margin (%)')