import sqlite3
import pandas as pd

con = sqlite3.connect("bank360.db")

# 1. Check customers
print("\n--- Customers (first 5) ---")
print(pd.read_sql("SELECT * FROM customers LIMIT 5;", con))

# 2. Check loans
print("\n--- Loans (first 5) ---")
print(pd.read_sql("SELECT * FROM loans LIMIT 5;", con))

# 3. Check transactions
print("\n--- Transactions (first 5) ---")
print(pd.read_sql("SELECT * FROM transactions LIMIT 5;", con))

# 4. Check credit cards
print("\n--- Credit Cards (first 5) ---")
print(pd.read_sql("SELECT * FROM credit_cards LIMIT 5;", con))

con.close()
