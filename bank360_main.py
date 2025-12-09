import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite
con = sqlite3.connect("bank360.db")

# ============================
# LOAD TABLES INTO PANDAS
# ============================
customers = pd.read_sql("SELECT * FROM customers", con)
loans = pd.read_sql("SELECT * FROM loans", con)
transactions = pd.read_sql("SELECT * FROM transactions", con)
credit_cards = pd.read_sql("SELECT * FROM credit_cards", con)

print("Data Loaded Successfully!")
print("Customers:", customers.shape)
print("Loans:", loans.shape)
print("Transactions:", transactions.shape)
print("Credit Cards:", credit_cards.shape)

# ============================
# MERGE DATASETS
# ============================
customer_loans = pd.merge(customers, loans, on="CustomerID", how="left")
customer_cards = pd.merge(customer_loans, credit_cards, on="CustomerID", how="left")
full_data = pd.merge(customer_cards, transactions, on="CustomerID", how="left")

print("\nMerged Dataset Shape:", full_data.shape)
print(full_data.head())

# ============================
# BASIC ANALYSIS
# ============================
print("\n--- Age Summary ---")
print(customers["Age"].describe())

print("\n--- Loan Amount Summary ---")
print(loans["LoanAmount"].describe())

print("\n--- Transaction Summary ---")
print(transactions["Amount"].describe())

# ============================
# VISUALIZATIONS
# ============================

# Age distribution
plt.figure(figsize=(8,4))
sns.histplot(customers["Age"], kde=True)
plt.title("Customer Age Distribution")
plt.show()

# Loan amount distribution
plt.figure(figsize=(8,4))
sns.histplot(loans["LoanAmount"], kde=True, color='green')
plt.title("Loan Amount Distribution")
plt.show()

# Transactions trend
plt.figure(figsize=(10,4))
transactions_sorted = transactions.sort_values("TransactionDate")
plt.plot(transactions_sorted["TransactionDate"], transactions_sorted["Amount"])
plt.xticks(rotation=45)
plt.title("Transaction Amount Over Time")
plt.show()

# Card type count
plt.figure(figsize=(6,4))
sns.countplot(x="CardType", data=credit_cards)
plt.title("Credit Card Types")
plt.show()

# ============================
# SAVE MERGED DATASET
# ============================
full_data.to_csv("full_merged_banking_data_from_sqlite.csv", index=False)
print("\nMerged dataset saved!")

# Close connection
con.close()
