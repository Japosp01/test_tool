import pandas as pd
import numpy as np

# get the data into python
xl=pd.ExcelFile("election_data2.xlsx")

#check things


print(xl.sheet_names)

df=xl.parse("Sheet1")

# show head of data
print(df.head())

#get total votes cast + descrptives

print(df.describe(include='all'))

# get percentage of votes by candidates


print(df['Candidate'].value_counts(normalize=True) * 100)

#just get counts with different function just for the joy of it
print(df.groupby('Candidate').size())
