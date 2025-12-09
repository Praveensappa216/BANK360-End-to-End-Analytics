import sqlite3

# Connect to SQLite database (creates file if not exists)
connection = sqlite3.connect("bank360.db")
cursor = connection.cursor()

# =============================
# CREATE CUSTOMERS TABLE
# =============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Gender TEXT,
    City TEXT,
    AccountType TEXT,
    AccountOpenDate TEXT
);
""")

# =============================
# CREATE LOANS TABLE
# =============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS loans (
    LoanID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    LoanAmount INTEGER,
    InterestRate REAL,
    TenureMonths INTEGER,
    LoanType TEXT,
    LoanStatus TEXT
);
""")

# =============================
# CREATE TRANSACTIONS TABLE
# =============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    TransactionID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    TransactionDate TEXT,
    TransactionType TEXT,
    Amount INTEGER,
    Merchant TEXT
);
""")

# =============================
# CREATE CREDIT CARDS TABLE
# =============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS credit_cards (
    CardID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    CardType TEXT,
    CreditLimit INTEGER,
    CurrentBalance INTEGER,
    LastPaymentDate TEXT,
    CardStatus TEXT
);
""")

connection.commit()
connection.close()

print("All tables created successfully in SQLite!")

