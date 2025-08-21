import pandas as pd
import numpy as np

# ---------------------------
# 1. CREATE / READ DATA
# ---------------------------
# Create DataFrame manually
data = {
    "OrderID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Region": ["North", "South", "East", "West", "North"],
    "Sales": [1200, 800, 400, 1500, np.nan],  # Missing value
    "Quantity": [1, 2, 3, 1, 4],
    "Date": pd.to_datetime(["2025-01-10", "2025-01-15", "2025-01-17", "2025-01-20", "2025-01-25"])
}
df = pd.DataFrame(data)

print("\n--- Original Data ---")
print(df)

# ---------------------------
# 2. VIEW DATA
# ---------------------------
print("\n--- Head & Tail ---")
print(df.head())       # First 5 rows
print(df.tail(2))      # Last 2 rows
print("99999999999999999999999999999999")
print("\n--- Info & Summary ---")
print(df.info())       # Data types & nulls
print(df.describe())   # Statistics

# ---------------------------
# 3. SELECT & FILTER
# ---------------------------
print("00000000000000000000")
print("\n--- Selecting columns ---")
print(df["Product"])              # Single column
print(df[["Product", "Sales"]])   # Multiple columns

print("\n--- Filtering rows ---")
print(df[df["Sales"] > 1000])     # Sales above 1000
print(df[(df["Sales"] > 800) & (df["Region"] == "North")])

# ---------------------------
# 4. SORTING
# ---------------------------
print("\n--- Sorting ---")
print(df.sort_values(by="Sales", ascending=False))

# ---------------------------
# 5. HANDLING MISSING DATA
# ---------------------------
print("\n--- Missing values ---")
print(df.isnull().sum())          # Count missing
df["Sales"].fillna(df["Sales"].mean(), inplace=True)  # Fill with mean

# ---------------------------
# 6. GROUPING & AGGREGATION
# ---------------------------
print("\n--- Group by Region ---")
print(df.groupby("Region")["Sales"].sum())  # Sum sales per region

print("\n--- Multiple aggregations ---")
print(df.groupby("Region").agg({"Sales": ["sum", "mean"], "Quantity": "sum"}))

# ---------------------------
# 7. ADDING / MODIFYING COLUMNS
# ---------------------------
df["Total"] = df["Sales"] * df["Quantity"]
print("\n--- Added Total column ---")
print(df)

# ---------------------------
# 8. MERGING / JOINING
# ---------------------------
extra_data = pd.DataFrame({
    "Region": ["North", "South", "East", "West"],
    "Manager": ["Alice", "Bob", "Charlie", "David"]
})
df = pd.merge(df, extra_data, on="Region", how="left")
print("\n--- After Merge ---")
print(df)

# ---------------------------
# 9. DATE OPERATIONS
# ---------------------------
df["Month"] = df["Date"].dt.month
print("\n--- Month Column ---")
print(df)

# ---------------------------
# 10. EXPORTING
# ---------------------------
df.to_csv("cleaned_sales.csv", index=False)
print("\nData saved to 'cleaned_sales.csv'")
