import pandas as pd
import numpy as np

# get the data into python
xl=pd.ExcelFile("bugetdata2d.xlsx")

print(xl.sheet_names)

df=xl.parse("Sheet1")

# show head of data
print(df.head())


#count rows and columns
print(df)


# summary statistics of character column
 
print(df.describe(include='all'))


# get sum for profit column
Total = df['Profit'].sum()
print (Total)

#gets moving average

MA=df.rolling(window=2)['Profit'].mean()
print (MA)

mav=MA.mean(axis = 0, skipna = True)

print(mav)

# create a new column 
df['MovAvg'] = df.rolling(window=2)['Profit'].mean()
  
# Print the DataFrame after  
# addition of new column 
print(df)

#get  summary stats

print(df.describe(include='all'))


#export results to text file

#np.savetxt(r'C:\Users\The Doctor\Desktop\python\pyhwnp.txt')


#df_MovAvg.to_csv('prob1.txt', sep='\t', index=False)

#export_csv = df.to_csv(r'C:\Users\The Doctor\Desktop\python\pyhwnp.txt'), index = None, header=True)



