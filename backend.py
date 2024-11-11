import sqlite3
import re

def create_connection():
    conn = sqlite3.connect("transactions.db")
    return conn

def initialize_db():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                           name TEXT PRIMARY KEY,
                           balance REAL,
                           username TEXT UNIQUE,
                           password TEXT
                       )''')
    
    # Predefined users with simpler names
    users = [
        ("Alice", 50000, "Alice", "123"),
        ("Bob", 50000, "Bob", "123"),
        ("Charlie", 50000, "Charlie", "123"),
        ("David", 50000, "David", "123"),
        ("Eve", 50000, "Eve", "123"),
        ("Frank", 50000, "Frank", "123"),
        ("Grace", 50000, "Grace", "123"),
        ("Hank", 50000, "Hank", "123"),
        ("Ivy", 50000, "Ivy", "123"),
        ("Jake", 50000, "Jake", "123")
    ]
    
    for name, balance, username, password in users:
        cursor.execute("INSERT OR IGNORE INTO accounts (name, balance, username, password) VALUES (?, ?, ?, ?)", 
                       (name, balance, username, password))
    
    conn.commit()
    conn.close()

def validate_login(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM accounts WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def add_user(name, balance, username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO accounts (name, balance, username, password) VALUES (?, ?, ?, ?)", 
                   (name, balance, username, password))
    conn.commit()
    conn.close()

def delete_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM accounts WHERE name=?", (name,))
    conn.commit()
    conn.close()

def update_balance(name, amount):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE name=?", (name,))
    result = cursor.fetchone()

    if result:
        new_balance = result[0] + amount
        cursor.execute("UPDATE accounts SET balance=? WHERE name=?", (new_balance, name))
    else:
        cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, amount))

    conn.commit()
    conn.close()

def get_balance(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE name=?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def user_exists(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM accounts WHERE name=?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def process_transaction(transcription, sender_name):
    words = transcription.split()
    amount = None
    receiver = None

    for i, word in enumerate(words):
        word = re.sub(r'[^\w\s]', '', word)  # Remove any punctuation
        if word.isdigit():
            amount = int(word)
        elif word.istitle() and word != sender_name:
            receiver = word

    if amount and receiver:
        if not user_exists(receiver):
            return f"User '{receiver}' does not exist. Please re-record the transaction.", None, None

        sender_balance_before = get_balance(sender_name)
        update_balance(sender_name, -amount)
        update_balance(receiver, amount)
        sender_balance_after = get_balance(sender_name)

        return f"Transaction of {amount} Rs from {sender_name} to {receiver} completed.", sender_balance_before, sender_balance_after
    else:
        return "Could not process the transaction. Please ensure the transcription includes a valid amount and receiver.", None, None
