# columns transformations in pandas 

import pandas as pd 

data = pd.read_excel("employee.xlsx")
print(data)

data.loc[(data["Bonus %"]== 0) , "GetBonus"]= "no bonus"
data.loc[(data["Bonus %"] > 0) , "GetBonus"]= "bonus"
print(data.head(10))

# add 2 columns 

df= pd.read_excel("sample.xlsx")
df["fullname"]= df["first name"]+" "+ df["last name"]
print(df)

print()

df["fullname"]= df["first name"].str.capitalize()+" "+ df["last name"].str.capitalize()
print(df)

# 20 % of salary as bonus

df["bonus"]= (df["salary"]/100)* 20
print(df)

# make short forms 

raw_data= {"months": ["january", "february", "march", "april"]}
data1= pd.DataFrame(raw_data)
print(data1)

def extract(value):
    return value[0:3]

data1["short name"]= data1["months"].map(extract)
print(data1)


# group by in pandas 

gp = data.groupby("Department").agg({"Employee ID": "count"})
print(gp)

print()

mp= data.groupby(["Department", "Gender"]).agg({"Employee ID": "count"})
print(mp)

x= data.groupby("Country").agg({"Age": "mean"})
print(x)

y= data.groupby("Country").agg({"Annual Salary": "mean"})
print(y)

z= data.groupby("Country").agg({"Annual Salary": "max"})
print(z)

m= z= data.groupby(["Country", "Gender"]).agg({"Annual Salary": "max"})
print(m)

'''merge, join, concatenate'''

data1= {"Emp_id": ["E01", "E02", "E03", "E04", "E05"],
        "Names": ["john", "ken", "siya", "riya", "priya"],
        "Age":[30, 24, 25, 28, 31]}

data2={"Emp_id": ["E01", "E02", "E03", "E04", "E05"],
        "Salary":[22000,30000,42000,56000,24000]}

df1= pd.DataFrame(data1)
df2= pd.DataFrame(data2)

print(df1)
print(df2)

print(pd.merge(df1, df2, on ="Emp_id"))
print(pd.merge(df1, df2, on ="Emp_id", how="right"))

# suppose there are null values , join are used
# {joins: left, right, outer, inner, cross}

con= pd.concat([df1, df2])
print(con)

'''to compare dataFrames'''

dict= {"Fruits": ["apple", "banana", "cheery", "papaya", "litchi"],
        "Prices": [180, 80,80, 45, 90],
        "Quantity":[10, 20, 15, 8, 12]}

data1= pd.DataFrame(dict)
print(data1)

data2= data1.copy()
print(data2)

# make changes

data2.loc[0, "Prices"]= 120
data2.loc[2, "Quantity"]= 16
data2.loc[3, "Prices"]= 50
data2.loc[4, "Quantity"]= 15

print(data2)
print(data1.compare(data2))

print(data1.compare(data2, align_axis=0, keep_shape=True))

'''pivoting and melting dataFrames'''

school= {"keys":[10, 20, 10, 20],
        "name":["jiya", "piya", "riya", "siya"], 
        "house": ["red", "yellow", "blue", "green"], 
        "grades": [8, 9, 10, 11]}

sc_data= pd.DataFrame(school)
print(sc_data)

print(sc_data.pivot(index="keys", columns= "name", values= ["house", "grades"]))

data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Store': ['A', 'B', 'A', 'B'],
    'Sales': [100, 200, 150, 250]
}

df = pd.DataFrame(data)
pivot_df = pd.pivot_table(df, values='Sales', index='Date', columns='Store', aggfunc='sum')
print(pivot_df)


# melting

school= {"name":["jiya", "piya", "riya", "siya"], 
        "house": ["red", "yellow", "blue", "green"], 
        "grades": [8, 9, 10, 11]}

sc_dt= pd.DataFrame(school)
print(pd.melt(sc_dt, id_vars= ["name"], value_vars=["house","grades"],var_name="House&Grade", value_name="values" ))

mdf = {'Date': ['2023-01-01', '2023-01-02'],
        'Store_A': [100, 150],
        'Store_B': [200, 250]
}

md = pd.DataFrame(mdf)
melted_df = pd.melt(md, id_vars=['Date'], value_vars=['Store_A', 'Store_B'], var_name='Store', value_name='Sales')
print(melted_df)
