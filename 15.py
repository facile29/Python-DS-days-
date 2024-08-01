import pandas as pd
import numpy as np 

'''creating DataFrame '''

data={"name": ["jiya", "monika", "gautam"], 
        "age" : [20, 21, 22], 
        "salary"  : [4000, 6000, 5000]}

df= pd.DataFrame(data)
print(df)

'''to import csv file'''

data= pd.read_csv("Rooms.csv")
print(data)

'''import excel file'''

a= pd.read_excel("EmployeeData_new.xlsx")
print(a)

# starting 10 data, by default it takes 5 data

print(a.head())
print(a.head(10))

# ending 10 data 

print(a.tail(10))

# information of file

print(a.info())

print(a.describe())

# to check null values

print(a.isnull())

print(a.isnull().sum())

# handling duplicates values

b= pd.read_excel("random.xlsx")

print(b)

print(b.duplicated())
print(b["EEID"].duplicated().sum())

print(b.drop_duplicates("EEID"))

# handling missing values 

print(b.isnull().sum())

b["Salary"]= b["Salary"].replace(np.nan, b["Salary"].mean())
print(b)

# backward and forward fill

print(b.fillna(method= "bfill"))
print(b.fillna(method= "ffill"))
