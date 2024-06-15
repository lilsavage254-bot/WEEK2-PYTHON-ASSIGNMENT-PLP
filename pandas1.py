import pandas as pd

# Create a simple DataFrame
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'Location': ['New York', 'Paris', 'Berlin', 'London'],
    'Age': [24, 13, 53, 33],
    'Hobby': ['Reading', 'Writing', 'Coding', 'Singing']
}

df = pd.DataFrame(data)
print(df)

# Read a CSV file   
df1 = pd.read_csv('vgsales.csv')
print(df1)

print(df1.describe())
print(df1.shape)

# Read an excel file.
excel1 = pd.read_excel("Book1.xlsx")
print(excel1) 

# Selecting data from a DataFrame
# Select a single column
df2 = df['name']
print(df2)

# Select multiple columns
df3 = df[['name', 'Location']]
print(df3)

df4 = df[['name', 'Location', 'Age']]
print(df4)

# Select rows by index.
df5 = df.loc[0]
print(df5)

# Select rows by condition
df6 = df[df['Age'] > 30]
print(df6)

# Adding new column to a Pandas dataframe.
df['Salary'] = [1000, 5000, 10000, 50000]
print(df)

df7 = df[['name', 'Age', 'Location', 'Salary']]
print(df7)

# Grouping data in a dataframe.
# Grouping by age and getting the average salary.
grouped = df.groupby("Age")["Salary"].mean()
print(grouped)