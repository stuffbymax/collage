Okay, here's a Pandas cheat sheet, designed to be both comprehensive and practical. I've organized it into logical sections for easier use.

**Pandas Cheat Sheet**

**I. Setup and Data Input/Output**

```python
import pandas as pd
import numpy as np # Often used with Pandas
```

**A. Reading Data**

*   **CSV:**
    ```python
    df = pd.read_csv("file.csv")          # Read from CSV
    df = pd.read_csv("file.csv", sep='\t') # Tab-separated
    df = pd.read_csv("file.csv", header=0) # Use row 0 as header
    df = pd.read_csv("file.csv", names=['col1', 'col2']) # Set custom headers
    df = pd.read_csv("file.csv", index_col=0) # Set column 0 as index
    ```

*   **Excel:**
    ```python
    df = pd.read_excel("file.xlsx", sheet_name='Sheet1')
    ```

*   **JSON:**
    ```python
    df = pd.read_json("file.json")
    ```

*   **SQL Database:**
    ```python
    import sqlite3
    conn = sqlite3.connect('database.db') # Or other database connectors
    query = "SELECT * FROM table_name"
    df = pd.read_sql_query(query, conn)
    ```

**B. Writing Data**

*   **CSV:**
    ```python
    df.to_csv("file.csv", index=False)      # Write to CSV, without index
    df.to_csv("file.csv", header=True)      # Write with header
    ```

*   **Excel:**
    ```python
    df.to_excel("file.xlsx", sheet_name='Sheet1', index=False)
    ```

*   **JSON:**
    ```python
     df.to_json("file.json", orient="records") # Write JSON, records format
    ```

*   **SQL Database:**
    ```python
    df.to_sql('table_name', conn, if_exists='replace', index=False)  # 'replace', 'append', 'fail'
    ```

**II. DataFrame Basics**

**A. Creating DataFrames**

*   **From Dictionary:**
    ```python
    data = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']}
    df = pd.DataFrame(data)
    ```
*   **From Lists:**
    ```python
    data = [[1, 'a'], [2, 'b'], [3, 'c']]
    df = pd.DataFrame(data, columns=['col1', 'col2'])
    ```
*   **From NumPy Array:**
    ```python
    data = np.array([[1, 2], [3, 4]])
    df = pd.DataFrame(data, columns=['col1', 'col2'])
    ```

**B. Inspecting DataFrames**

*   `df.head(n)`: First `n` rows (default: 5)
*   `df.tail(n)`: Last `n` rows (default: 5)
*   `df.shape`: (rows, columns) as tuple
*   `df.info()`: Data types, non-null counts, memory usage
*   `df.describe()`: Descriptive statistics (count, mean, std, etc.)
*   `df.columns`: List of column labels
*   `df.index`: Index labels
*   `df.dtypes`: Data types of each column
*   `df.isnull().sum()`: Sum of null values per column
*   `df.nunique()`: Number of unique values per column

**III. Selecting Data**

**A. By Label (Columns and Rows)**

*   `df['column_name']` or `df.column_name`: Single column (Series)
*   `df[['col1', 'col2']]`: Multiple columns (DataFrame)
*   `df.loc[row_label]`: Single row by label
*   `df.loc[row_label1:row_label2]`: Range of rows by label
*   `df.loc[row_label, 'col1']`: Single cell by label
*   `df.loc[:, 'col1']`: All rows, column 'col1'
*   `df.loc[df['col1'] > 5, ['col2', 'col3']]`: Conditional selection with labels

**B. By Position (Integer Index)**

*   `df.iloc[row_index]`: Single row by index
*   `df.iloc[row_index1:row_index2]`: Range of rows by index
*   `df.iloc[row_index, col_index]`: Single cell by index
*   `df.iloc[:, col_index]`: All rows, column by index
*   `df.iloc[[0, 2, 4], [1, 3]]`: Specific rows and columns by index
*   `df.iloc[0]`: Accessing the first row

**C. Conditional Selection (Boolean Masking)**

*   `df[df['col1'] > 5]`: Filter rows where 'col1' > 5
*   `df[(df['col1'] > 5) & (df['col2'] == 'a')]`:  Multiple conditions (&, |, ~)
*   `df[df['col1'].isin([1, 3, 5])]`: Filter based on values in list
*   `df[df['col1'].str.contains('pattern')]`: String matching

**IV. Data Manipulation**

**A. Adding/Removing Columns**

*   `df['new_col'] = value`: Add new column with scalar value
*   `df['new_col'] = df['col1'] * 2`: Add computed column
*   `df.insert(loc, column, value)`: Insert column at position
*   `df.drop(columns=['col1', 'col2'])`: Drop columns
*   `df.drop('col1', axis=1)`: Same, but using axis=1

**B. Renaming Columns/Index**

*   `df.rename(columns={'old_name': 'new_name'})`
*   `df.rename(columns=lambda x: x.upper())`: Function to rename
*   `df.rename(index={0: 'row_1', 1: 'row_2'})`
*   `df.set_index('col1', inplace=True)`: Set column as index
*   `df.reset_index(inplace=True)`: Reset index to default integer index

**C. Handling Missing Values**

*   `df.isnull()`: Boolean mask of null values
*   `df.dropna()`: Drop rows with any null values
*   `df.dropna(subset=['col1'])`: Drop rows with null values in 'col1'
*   `df.fillna(value)`: Fill null values with `value`
*   `df.fillna(method='ffill')`: Fill forward from last value
*   `df.fillna(df.mean())`: Fill with column mean
*   `df.replace(to_replace=np.nan, value=0)`: Replace NaN values with 0

**D. Data Transformation**

*   `df['col'].astype(dtype)`: Change data type (int, float, str, datetime)
*   `df['col'].apply(function)`: Apply a function to column values
*   `df['col'].map(mapping_dict)`: Map values using a dictionary
*   `df['col'].apply(lambda x: x * 2)`: Lambda for inline functions
*   `df['col'].str.upper()`: String methods (upper, lower, split, etc.)
*   `df.applymap(function)`: Apply a function to every cell in the DataFrame

**E. Sorting and Ordering**

*   `df.sort_values(by='col1')`: Sort by column 'col1'
*   `df.sort_values(by=['col1', 'col2'], ascending=[True, False])`: Multi-sort
*   `df.sort_index()`: Sort by index

**V. Data Aggregation and Grouping**

*   `df['col'].value_counts()`: Frequency of unique values in column
*   `df.groupby('col1').mean()`: Group by 'col1', get mean of numeric columns
*   `df.groupby('col1')['col2'].sum()`: Group by 'col1', sum of 'col2'
*   `df.groupby('col1').agg({'col2': 'sum', 'col3': 'mean'})`: Aggregation using multiple functions
*   `df.pivot_table(index='col1', columns='col2', values='col3')`: Create a pivot table
*   `df.groupby('col1').size()`: Number of items in each group

**VI. Combining DataFrames**

*   `pd.concat([df1, df2])`: Combine vertically (row-wise)
*   `pd.concat([df1, df2], axis=1)`: Combine horizontally (column-wise)
*   `pd.merge(df1, df2, on='key')`: Merge on common column 'key'
*   `pd.merge(df1, df2, on=['key1', 'key2'])`: Merge on multiple keys
*   `pd.merge(df1, df2, left_on='lkey', right_on='rkey')`: Merge using different key names
*   `pd.merge(df1, df2, how='left')`: Left join
*   `pd.merge(df1, df2, how='right')`: Right join
*   `pd.merge(df1, df2, how='outer')`: Outer join
*   `pd.merge(df1, df2, how='inner')`: Inner join (default)
*   `df1.join(df2, on='key', how='left')`: Similar to merge, for indexed data

**VII. Time Series**

*   `pd.to_datetime(df['date_col'])`: Convert strings to datetime
*   `df['date_col'] = pd.to_datetime(df['date_col'], format="%Y-%m-%d")`: Specify format
*   `df['date_col'].dt.year`: Access year, month, day, hour, etc.
*   `df.set_index('date_col', inplace=True)`: Set date column as index
*   `df.resample('M').mean()`: Resample to monthly, compute mean
*   `df.resample('D').sum()`: Resample to daily, compute sum

**VIII. Other Useful Functions**

*   `df.copy()`: Create a deep copy of the DataFrame
*   `df.apply(lambda x: x.max() - x.min(), axis=1)`: Column max - min, applying to rows
*   `pd.cut(df['col'], bins)`: Bin values into discrete intervals
*   `pd.qcut(df['col'], q)`: Bin values into quantiles
*   `df.groupby('group_column')['target_column'].transform('mean')` Transform to make a new column based on group mean.

**Notes**

*   This is a cheat sheet, not a full tutorial. Refer to the Pandas documentation for detailed usage.
*   `inplace=True` modifies the DataFrame in place instead of creating a copy.
*   `axis=0` refers to rows, `axis=1` refers to columns.
*   Remember to always explore and understand your data before applying transformations.

**How to Use This Cheat Sheet**

1.  **Keep it handy:** Save this cheat sheet or print it out for quick reference.
2.  **Search:** Use `Ctrl+F` (or `Cmd+F`) to quickly search for specific functions or operations.
3.  **Experiment:** Don't just read it, try out the code snippets with your own data to get a feel for how they work.
4.  **Refer to Documentation:** If you need more details on any function, consult the official Pandas documentation.

I hope you find this comprehensive cheat sheet useful! Good luck with your data analysis!
