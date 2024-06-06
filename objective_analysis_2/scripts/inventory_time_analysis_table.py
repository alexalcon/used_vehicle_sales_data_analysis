import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.table as tbl

# load the inventory time data
file_path = "../data/inventory_time_by_brand_model.csv"
df = pd.read_csv(file_path)

# create a table from the DataFrame
fig, ax = plt.subplots(figsize=(12, 8))  # Set the size of the figure
ax.axis('off')  # Remove the axes

# create the table
table = tbl.table(ax, cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# set table style
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.2)

# adjust layout to reduce space between title and table
plt.subplots_adjust(top=0.95)  # Adjust this value to reduce space

# add title
plt.title('Profit by Brand and Model Table', pad=5)  # Reduce padding here

# save the table as an image
output_file_path = '../results/inventory_time_by_brand_and_model_table.png'
plt.savefig(output_file_path, bbox_inches='tight', dpi=300)

print(f"Table saved as {output_file_path}")
