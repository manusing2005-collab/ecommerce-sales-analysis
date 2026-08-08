import pandas as pd
import random
from datetime import datetime, timedelta

products = {
    "Laptop": ("Electronics", 55000),
    "Mobile": ("Electronics", 25000),
    "Headphones": ("Electronics", 3000),
    "Keyboard": ("Accessories", 1500),
    "Mouse": ("Accessories", 800),
    "Monitor": ("Electronics", 12000),
    "Backpack": ("Fashion", 2000),
    "Shoes": ("Fashion", 3500),
    "T-Shirt": ("Fashion", 1000),
    "Watch": ("Fashion", 5000)
}

cities = ["Mumbai", "Pune", "Delhi", "Bangalore", "Chennai", "Hyderabad"]

data = []

start_date = datetime(2026, 1, 1)

for i in range(1, 501):

    product = random.choice(list(products.keys()))
    category, price = products[product]

    date = start_date + timedelta(days=random.randint(0, 180))

    quantity = random.randint(1, 5)

    city = random.choice(cities)

    data.append([
        i,
        date.strftime("%Y-%m-%d"),
        product,
        category,
        city,
        quantity,
        price
    ])

df = pd.DataFrame(data, columns=[
    "Order_ID",
    "Date",
    "Product",
    "Category",
    "City",
    "Quantity",
    "Price"
])

df.to_csv("sales.csv", index=False)

print("Dataset created successfully!")
print(df.head())