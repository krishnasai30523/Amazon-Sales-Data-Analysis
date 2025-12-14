import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------
# Load Dataset
# ----------------------------------
file_path = r"C:\Users\krish\OneDrive\Desktop\UnifiedMentor_Internship\Projects\Amazon_Sales_Data\datasets\amazon_sales.csv"
df = pd.read_csv(file_path)

# ----------------------------------
# Basic Data Check
# ----------------------------------
print("First 5 records:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# ----------------------------------
# Data Preprocessing
# ----------------------------------
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()

# ----------------------------------
# Total Sales Revenue
# ----------------------------------
total_sales = df['Total Sales'].sum()
print("\nTotal Sales Revenue:", total_sales)

# ----------------------------------
# Category-wise Sales
# ----------------------------------
category_sales = df.groupby('Category')['Total Sales'].sum()
print("\nCategory-wise Sales:")
print(category_sales)

category_sales.plot(kind='bar')
plt.title("Category-wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# ----------------------------------
# Region-wise Sales
# ----------------------------------
region_sales = df.groupby('Region')['Total Sales'].sum()
print("\nRegion-wise Sales:")
print(region_sales)

region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Region-wise Sales Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# ----------------------------------
# Monthly Sales Trend
# ----------------------------------
monthly_sales = df.groupby('Month')['Total Sales'].sum()
print("\nMonthly Sales Trend:")
print(monthly_sales)

monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------
# Top 5 Selling Products
# ----------------------------------
top_products = (
    df.groupby('Product')['Total Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Selling Products:")
print(top_products)

top_products.plot(kind='bar')
plt.title("Top 5 Selling Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# ----------------------------------
# Conclusion
# ----------------------------------
print("\nConclusion:")
print("- Electronics category generates the highest revenue.")
print("- Certain regions contribute more to overall sales.")
print("- Sales show a positive trend across months.")
print("- A few products dominate total revenue.")


