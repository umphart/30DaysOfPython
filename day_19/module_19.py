import pandas as pd

# Part 1: Load the hacker_news.csv file into a Pandas DataFrame
file_path = './data/hacker_news.csv'  # Adjust the path if necessary
df = pd.read_csv(file_path)

# Part 2: Get the first five rows
print("First five rows:")
print(df.head())

# Part 3: Get the last five rows
print("\nLast five rows:")
print(df.tail())

# Part 4: Get the 'title' column as a pandas series
print("\nTitle column as Pandas Series:")
title_column = df['title']
print(title_column.head())

# Part 5: Count the number of rows and columns
print("\nNumber of rows and columns:")
rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")

# Part 6: Filter titles which contain 'Python'
print("\nTitles which contain 'Python':")
python_titles = df[df['title'].str.contains('Python', case=False, na=False)]
print(python_titles[['title']].head())

# Part 7: Filter titles which contain 'JavaScript'
print("\nTitles which contain 'JavaScript':")
js_titles = df[df['title'].str.contains('JavaScript', case=False, na=False)]
print(js_titles[['title']].head())

# Part 8: Explore the data and make sense of it
# Print the general info about the dataframe
print("\nDataFrame Information:")
print(df.info())

# Get descriptive statistics for numeric columns
print("\nDescriptive statistics for numeric columns:")
print(df.describe())

# Check for any missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Explore the unique values in a few columns
print("\nUnique values in the 'type' column:")
print(df['type'].unique())

# Let's check the first few rows again with all columns
print("\nFirst few rows with all columns:")
print(df.head())
