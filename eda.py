import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    "Retail_Transactions_Dataset.xlsx",
    engine="openpyxl"
)

df['Date'] = pd.to_datetime(df['Date'])


df['Year'] = df['Date'].dt.year

sales_by_year = df.groupby('Year')['Total_Cost'].sum()

print("Total Sales by Year:")
print(sales_by_year)

sales_by_year.plot(kind='line')
plt.title("Total Sales Over Years")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.show()

customer_sales = df.groupby('Customer_Category')['Total_Cost'].sum()

print("\nTotal Sales by Customer Category:")
print(customer_sales)

customer_sales.plot(kind='bar')
plt.title("Sales by Customer Category")
plt.xlabel("Customer Category")
plt.ylabel("Total Sales")
plt.show()


top_products = (
    df.groupby('Product')['Total_Cost']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Sales:")
print(top_products)

top_products.plot(kind='bar')
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

print("\n--- FINAL BUSINESS INSIGHTS ---")
print("1. Sales remained stable from 2020–2023 with a drop in 2024 due to partial data.")
print("2. Customer sales are evenly distributed across categories.")
print("3. One product significantly outperforms others in total sales.")
print("4. Promotions are not applied to all transactions, indicating scope for targeted offers.")




