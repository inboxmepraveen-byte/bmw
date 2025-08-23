import datetime
import pandas as pd
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