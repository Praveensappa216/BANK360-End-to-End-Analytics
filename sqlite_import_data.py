import sqlite3
import pandas as pd

# Connect to SQLite database
connection = sqlite3.connect("bank360.db")

# Load CSV files with pandas
customers = pd.read_csv("customers.csv")
loans = pd.read_csv("loans.csv")
transactions = pd.read_csv("transactions.csv")
credit_cards = pd.read_csv("credit_cards.csv")

# Insert into SQLite using pandas .to_sql()
customers.to_sql("customers", connection, if_exists="append", index=False)
loans.to_sql("loans", connection, if_exists="append", index=False)
transactions.to_sql("transactions", connection, if_exists="append", index=False)
credit_cards.to_sql("credit_cards", connection, if_exists="append", index=False)

connection.commit()
connection.close()

print("All CSV data imported successfully into SQLite!")
