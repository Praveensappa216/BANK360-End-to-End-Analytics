import pandas as pd

# Load datasets
customers = pd.read_csv("customers.csv")
loans = pd.read_csv("loans.csv")
transactions = pd.read_csv("transactions.csv")
credit_cards = pd.read_csv("credit_cards.csv")

print("Customers Data:")
print(customers.head())

print("\nLoans Data:")
print(loans.head())

print("\nTransactions Data:")
print(transactions.head())

print("\nCredit Cards Data:")
print(credit_cards.head())

print("\n===== DATASET SHAPES =====")
print("Customers:", customers.shape)
print("Loans:", loans.shape)
print("Transactions:", transactions.shape)
print("Credit Cards:", credit_cards.shape)

print("\n===== NULL VALUES =====")
print("Customers:\n", customers.isnull().sum())
print("\nLoans:\n", loans.isnull().sum())
print("\nTransactions:\n", transactions.isnull().sum())
print("\nCredit Cards:\n", credit_cards.isnull().sum())

print("\n===== SUMMARY STATS =====")
print(customers.describe())
print(loans.describe())
print(transactions.describe())
print(credit_cards.describe())

# ==========================================
# MERGE ALL DATASETS INTO ONE MASTER TABLE
# ==========================================

print("\n===== MERGING DATASETS =====")

# Merge Customers + Loans
customer_loans = pd.merge(customers, loans, on="CustomerID", how="left")

# Merge with Credit Cards
customer_loans_cards = pd.merge(customer_loans, credit_cards, on="CustomerID", how="left")

# Merge with Transactions (many transactions per customer)
full_data = pd.merge(customer_loans_cards, transactions, on="CustomerID", how="left")

print("\nMerged Dataset Shape:", full_data.shape)

print("\n===== MERGED DATA SAMPLE =====")
print(full_data.head())

# Save merged file
full_data.to_csv("full_merged_banking_data.csv", index=False)
print("\nMerged dataset saved as: full_merged_banking_data.csv")


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8,5))
sns.histplot(customers["Age"], kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(loans["LoanAmount"], kde=True, color="green")
plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(data=loans, x="LoanStatus")
plt.title("Loan Status Count")
plt.xlabel("Status")
plt.ylabel("Number of Loans")
plt.show()

transactions_sorted = transactions.sort_values("TransactionDate")

plt.figure(figsize=(10,5))
plt.plot(transactions_sorted["TransactionDate"], transactions_sorted["Amount"])
plt.title("Transactions Amount Trend Over Time")
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Amount")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(data=credit_cards, x="CardType")
plt.title("Credit Card Type Distribution")
plt.xlabel("Card Type")
plt.ylabel("Count")
plt.show()
print("/nvisualizations generated.")