#To create a Pandas DataFrame in Python, you can use the pandas.DataFrame() constructor. Here are three common ways to create a DataFrame:

#1. From a Dictionary
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)


#2. from a List of Lists
import pandas as pd

data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)


#3. from a List of Dictionaries
import pandas as pd

data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]
df = pd.DataFrame(data)
print(df)


#Each method is flexible and can be adapted based on the structure of your data.
