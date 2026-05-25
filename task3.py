# Marketing Funnel & Conversion Analysis - Task 3

import pandas as pd
import matplotlib.pyplot as plt

# Sample marketing funnel data
data = {
    "Stage": ["Website Visit", "Product View", "Add to Cart", "Checkout", "Purchase"],
    "Users": [5000, 3500, 2000, 1200, 800]
}

# Create dataframe
df = pd.DataFrame(data)

# Display data
print("Marketing Funnel Data")
print(df)

# Conversion rate calculation
conversion_rates = []

for i in range(1, len(df)):
    rate = (df["Users"][i] / df["Users"][i-1]) * 100
    conversion_rates.append(rate)

# Print conversion rates
print("\nConversion Rates:")
for i in range(1, len(df)):
    print(df["Stage"][i-1], "to", df["Stage"][i], "=", round(conversion_rates[i-1], 2), "%")

# Total conversion rate
total_conversion = (df["Users"].iloc[-1] / df["Users"].iloc[0]) * 100

print("\nOverall Conversion Rate:", round(total_conversion, 2), "%")

# Funnel graph
plt.figure(figsize=(8,5))
plt.plot(df["Stage"], df["Users"], marker='o')

plt.title("Marketing Funnel Analysis")
plt.xlabel("Funnel Stage")
plt.ylabel("Number of Users")

plt.grid(True)

plt.show()

# Bar chart
plt.figure(figsize=(8,5))
plt.bar(df["Stage"], df["Users"])

plt.title("Users at Each Funnel Stage")
plt.xlabel("Stages")
plt.ylabel("Users")

plt.show()

# Insights
print("\nKey Insights:")
print("- Highest drop-off occurs between Product View and Add to Cart")
print("- Checkout stage needs optimization")
print("- Improve marketing campaigns for better conversions")
print("- Simplify purchase process to increase sales")
