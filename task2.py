# Customer Retention & Churn Analysis - Task 2

import pandas as pd
import matplotlib.pyplot as plt

# Sample customer data
data = {
    "Customer_ID": [101,102,103,104,105,106,107,108],
    "Subscription_Months": [12, 5, 8, 2, 15, 6, 3, 10],
    "Plan": ["Premium","Basic","Premium","Basic","Premium","Basic","Basic","Premium"],
    "Region": ["South","North","East","West","South","East","North","West"],
    "Churn": ["No","Yes","No","Yes","No","Yes","Yes","No"]
}

# Create dataframe
df = pd.DataFrame(data)

# Display dataset
print("Customer Dataset")
print(df)

# Total customers
total_customers = len(df)

# Churn customers
churn_customers = len(df[df["Churn"] == "Yes"])

# Retained customers
retained_customers = len(df[df["Churn"] == "No"])

# Churn rate
churn_rate = (churn_customers / total_customers) * 100

print("\nTotal Customers:", total_customers)
print("Churn Customers:", churn_customers)
print("Retained Customers:", retained_customers)
print("Churn Rate: {:.2f}%".format(churn_rate))

# Plan-wise churn analysis
plan_churn = df.groupby("Plan")["Churn"].value_counts()

print("\nPlan-wise Churn Analysis")
print(plan_churn)

# Average customer lifetime
avg_lifetime = df["Subscription_Months"].mean()

print("\nAverage Customer Lifetime:", avg_lifetime)

# Churn graph
churn_counts = df["Churn"].value_counts()

plt.figure(figsize=(6,5))
plt.bar(churn_counts.index, churn_counts.values)

plt.title("Customer Churn Analysis")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")

plt.show()

# Subscription trend graph
plt.figure(figsize=(8,5))
plt.plot(df["Customer_ID"], df["Subscription_Months"], marker='o')

plt.title("Customer Lifetime Trend")
plt.xlabel("Customer ID")
plt.ylabel("Subscription Months")

plt.grid(True)

plt.show()

# Business recommendations
print("\nRecommendations:")
print("- Improve customer support")
print("- Offer discounts for long-term users")
print("- Provide loyalty rewards")
print("- Focus on Basic plan customers to reduce churn")
