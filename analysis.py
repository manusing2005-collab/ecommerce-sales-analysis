import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales.csv")

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate Revenue
df["Revenue"] = df["Quantity"] * df["Price"]


# -----------------------------
# DATA INSPECTION
# -----------------------------

print("DATA TYPES:")
print(df.dtypes)

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATES:")
print(df.duplicated().sum())


# -----------------------------
# TOTAL REVENUE
# -----------------------------

total_revenue = df["Revenue"].sum()

print("\nTOTAL REVENUE:")
print(f"₹{total_revenue:,}")


# -----------------------------
# REVENUE BY PRODUCT
# -----------------------------

product_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nREVENUE BY PRODUCT:")
print(product_revenue)


# -----------------------------
# REVENUE BY CITY
# -----------------------------

city_revenue = (
    df.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nREVENUE BY CITY:")
print(city_revenue)


# -----------------------------
# REVENUE BY CATEGORY
# -----------------------------

category_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nREVENUE BY CATEGORY:")
print(category_revenue)


# -----------------------------
# MONTHLY REVENUE
# -----------------------------

df["Month"] = df["Date"].dt.to_period("M")

monthly_revenue = (
    df.groupby("Month")["Revenue"]
    .sum()
)

print("\nREVENUE BY MONTH:")
print(monthly_revenue)


# -----------------------------
# CHART 1: REVENUE BY PRODUCT
# -----------------------------

product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/revenue_by_product.png")
plt.show()

plt.close()


# -----------------------------
# CHART 2: REVENUE BY CITY
# -----------------------------

city_revenue.plot(kind="bar")

plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/revenue_by_city.png")
plt.show()

plt.close()


# -----------------------------
# CHART 3: REVENUE BY CATEGORY
# -----------------------------

category_revenue.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/revenue_by_category.png")
plt.show()

plt.close()


# -----------------------------
# CHART 4: MONTHLY REVENUE
# -----------------------------

monthly_revenue.plot(kind="line", marker="o")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/monthly_revenue.png")
plt.show()

plt.close()


# -----------------------------
# KEY INSIGHTS
# -----------------------------

top_product = product_revenue.idxmax()
top_product_revenue = product_revenue.max()

top_city = city_revenue.idxmax()
top_city_revenue = city_revenue.max()

top_category = category_revenue.idxmax()
top_category_revenue = category_revenue.max()

best_month = monthly_revenue.idxmax()
best_month_revenue = monthly_revenue.max()


print("\n--- KEY INSIGHTS ---")

print(f"Top Product: {top_product}")
print(f"Revenue: ₹{top_product_revenue:,}")

print(f"\nTop City: {top_city}")
print(f"Revenue: ₹{top_city_revenue:,}")

print(f"\nTop Category: {top_category}")
print(f"Revenue: ₹{top_category_revenue:,}")

print(f"\nBest Month: {best_month}")
print(f"Revenue: ₹{best_month_revenue:,}")