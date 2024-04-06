# Importing necessary libraries
import pandas as pd
import numpy as np

# Sample data (usually, you would load data from a file or database)
data = {
    'Sales': [250, 150, 200, 300],
    'Marketing Spend': [100, 50, 80, 120],
    'Location': ['East', 'West', 'North', 'South']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Basic Data Analysis
print("Total Sales:", df['Sales'].sum())
print("Average Marketing Spend:", df['Marketing Spend'].mean())
print("Sales Variance:", df['Sales'].var())
print("Locations:", ', '.join(df['Location'].unique()))
