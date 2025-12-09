import os
print("Database Path:", os.path.abspath("bank360.db"))


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================
# STEP 1 — CONNECT TO SQLITE DATABASE
# =========================================
con = sqlite3.connect("bank360.db")
print("Connected to SQLite database!")

# =========================================
# STEP 2 — LOAD TABLES INTO PANDAS
# =========================================
customers = pd.read_sql("SELECT * FROM customers", con)
loans = pd.read_sql("SELECT * FROM loans", con)
transactions = pd.read_sql("SELECT * FROM transactions", con)
credit_cards = pd.read_sql("SELECT * FROM credit_cards", con)

print("\nData Loaded:")
print("Customers:", customers.shape)
print("Loans:", loans.shape)
print("Transactions:", transactions.shape)
print("Credit Cards:", credit_cards.shape)

# =========================================
# STEP 3 — MERGE ALL TABLES
# =========================================
customer_loans = pd.merge(customers, loans, on="CustomerID", how="left")
customer_cards = pd.merge(customer_loans, credit_cards, on="CustomerID", how="left")
full_data = pd.merge(customer_cards, transactions, on="CustomerID", how="left")

print("\nMerged Dataset Shape:", full_data.shape)
print(full_data.head())

# =========================================
# STEP 4 — BASIC ANALYSIS
# =========================================
print("\n====================")
print("SUMMARY STATISTICS")
print("====================")
print("\nAge Distribution:\n", customers["Age"].describe())
print("\nLoan Amount Stats:\n", loans["LoanAmount"].describe())
print("\nTransaction Amount Stats:\n", transactions["Amount"].describe())

# =========================================
# STEP 5 — VISUAL GRAPHS
# =========================================

# Age distribution
plt.figure(figsize=(8,4))
sns.histplot(customers["Age"], kde=True)
plt.title("Customer Age Distribution")
plt.show()

# Loan amount distribution
plt.figure(figsize=(8,4))
sns.histplot(loans["LoanAmount"], kde=True, color="green")
plt.title("Loan Amount Distribution")
plt.show()

# Card types
plt.figure(figsize=(6,4))
sns.countplot(x="CardType", data=credit_cards)
plt.title("Credit Card Types")
plt.show()

# Monthly transactions
transactions["TransactionDate"] = pd.to_datetime(transactions["TransactionDate"])
monthly_spend = transactions.groupby(transactions["TransactionDate"].dt.to_period("M"))["Amount"].sum()

plt.figure(figsize=(10,4))
monthly_spend.plot(kind="line")
plt.title("Monthly Total Transaction Amount")
plt.xticks(rotation=45)
plt.show()

# =========================================
# STEP 6 — SAVE MERGED DATASET
# =========================================
full_data.to_csv("bank360_final_output.csv", index=False)
print("\nFinal merged file saved as: bank360_final_output.csv")

# =========================================
# STEP 7 — RUN SQL QUERIES INSIDE PYTHON
# =========================================
print("\n====================")
print("SQL QUERY RESULTS")
print("====================")

top_merchants = pd.read_sql("""
SELECT Merchant, SUM(Amount) AS TotalSpent
FROM transactions
GROUP BY Merchant
ORDER BY TotalSpent DESC
LIMIT 5;
""", con)

print("\nTop Merchants:\n", top_merchants)

# Close connection
con.close()
print("\nPipeline completed successfully!")
