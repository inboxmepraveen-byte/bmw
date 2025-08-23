import pandas as pd
import datetime

# Load dataset
df = pd.read_csv("BMW_Car_Sales_Classification.csv")  # read_csv is a function that reads the file and return the dataframe
print(df)
print()



print("1️⃣ Understanding Your Data (Exploratory Data Analysis – EDA")

print(df.head())  # See first 5 rows
print(df.info()) # shows column names,non null count and data types
print(df.shape)  # shows the number of rows and column in the dataset as (row,column)
print(df.isnull().sum()) # to show the null values and count the values in the column
print(df["Model"].unique())  # Example: all car models in dataset / To access a specific column, you use its name inside square brackets.
print(df.describe()) # for numeric column / count,mean,min,max,25,50,75,std.
print(df.sample(n=5)) # to print any 5 random rows by default
print(df.columns) # shows all the column names

print("️⃣ Working with Unique Values")

print(df["Color"].unique()) # unlike duplilcates print the unique colors
print(df["Color"].nunique()) # the number of unique colors
print(df["Color"].value_counts()) # Tells you frequency of each color in the dataset  

print("️⃣ Cleaning & Preparing Data")

df=(df.drop_duplicates())  # drop the row if the value in the rows is same that repeat for all column
df["Sales_Volume"]=df["Sales_Volume"].fillna(0) # replace the null values by the value given 
df=df.rename(columns={"Sales_Volume":"sales"}) #only changes the name of the column 
df=df.replace(value={"":"unknown"}) #replaces the value inside the column
print(df["Year"].dtype)
if df["Year"].dtype!="int":
    df["Year"]=df["Year"].astype(int) 

print("4️⃣ Filtering & Sorting")

print(df[df["Engine_Size_L"]>4.2]) #inbra create T or F mask/ outbra selects the rows that are T 
print(df["Engine_Size_L"].dtype)
print(df.sort_values(by="Year",ascending=True)) # used to short rows by column 
print(df.query("sales > 9990 and Model=='5 Series'")) # filtering rows with conditions in a SQL-like style

print("️⃣ Grouping & Aggregation")

print(df.groupby("Model")["Price_USD"].mean()) # groupby() is a method and the [is the price selection]
print(df.groupby(["Model", "Region"]).agg({"sales": "sum"})) # grouping on multiple columns and aggregation
pivot = df.pivot_table(
    index="Model",         # show in rows
    columns="Region",      # show in column
    values="sales",        # data to summarize
    aggfunc="sum"          # how to summarize
)


print(pivot)

import pandas as pd

print("6️⃣ Combining Data")

df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

# Append rows
result = pd.concat([df1, df2], axis=0) # concate df2 below df1 
print(result)


df1 = pd.DataFrame({"ID": [1, 2],
                    "Name": ["A", "B"]})
df2 = pd.DataFrame({"ID": [2, 1],
                     "Age": [20, 30]})

# Merge on ID
result = df1.merge(df2, on="ID") # Combine DataFrames based on common columns (like SQL joins).
print(result) 

df1 = pd.DataFrame({"Name": ["A", "B"]}, index=[2,1])
df2 = pd.DataFrame({"Age": [20, 30]}, index=[1, 2])

result = df1.join(df2)
print(result)                      # concat → Pasting sheets of paper together.
                                   # merge → Connecting tables by a common key, like SQL.
                                   # join → Matching items by their row numbers (index).

print("7️⃣ Working with Dates  ")

current=datetime.datetime.now()
print(current)

print(datetime.date.today())
print(datetime.datetime(2026,11,9,12,00))
print()

df = pd.DataFrame({
    "Order_Date": ["2024-01-01", "2024-01-05", "2024-02-10"],
    "Sales": [200, 150, 300]
})

# Convert to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
print(df.dtypes)

df["Yeer"]=df["Order_Date"].dt.year                                                                                                         
df["Month"]=df["Order_Date"].dt.month                                                                                                         
df["day"]=df["Order_Date"].dt.day
df["day_name"]=df["Order_Date"].dt.day_name()

print(df)

print(df[df["Order_Date"]>"2024-02-01"])

dates = pd.date_range(start="2024-01-01", end="2024-01-07", freq="D")
print(dates)

df["Days_Since"] = df["Order_Date"] - df["Order_Date"].min()
print(df)

df.to_excel("updated_sales.xlsx",index=False)