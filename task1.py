# Business Sales Performance Analytics - Task 1

import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 18000, 17000, 22000, 25000],
    "Profit": [3000, 4000, 5000, 4500, 6000, 7000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display data
print("Business Sales Data")
print(df)

# Total sales and profit
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)

# Highest sales month
highest_sales = df.loc[df["Sales"].idxmax()]

print("\nHighest Sales Month:")
print(highest_sales)

# Line graph for Sales
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker='o')

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.show()

# Bar graph for Profit
plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Profit"])

plt.title("Monthly Profit Analysis")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.show()
