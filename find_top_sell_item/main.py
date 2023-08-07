import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data into a Pandas DataFrame
df = pd.read_csv('finance_liquor_date16-19-full.csv')

# Aggregate data by zip code and item
zip_item_sales = df.groupby(['zip_code', 'item_description'])['bottles_sold'].sum().reset_index()

# Find the most popular item by zip code
most_popular_item = zip_item_sales.groupby('zip_code').apply(lambda group: group[group['bottles_sold'] == group['bottles_sold'].max()])

# Create a scatter plot using Seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(data=most_popular_item, x='zip_code', y='bottles_sold', hue='item_description', palette='viridis', s=100, marker='o')

plt.title('Most Popular Item by Zip Code')
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')

# Move the legend to the side
plt.legend(title='item_description', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to prevent cutting off the plot
plt.tight_layout()

plt.show()

