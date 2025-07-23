# Functions to work with SQLite

import sqlite3

def init_db():
    conn = sqlite3.connect("recipes.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    amount TEXT
                )''')
    conn.commit()
    conn.close()

def add_ingredient(name, amount):
    conn = sqlite3.connect("recipes.db")
    c = conn.cursor()
    c.execute("INSERT INTO ingredients (name, amount) VALUES (?, ?)", (name, amount))
    conn.commit()
    conn.close()

def get_ingredients():
    conn = sqlite3.connect("recipes.db")
    c = conn.cursor()
    c.execute("SELECT name, amount FROM ingredients")
    results = c.fetchall()
    conn.close()
    return results

def delete_ingredient(name):
    conn = sqlite3.connect("recipes.db")
    c = conn.cursor()
    c.execute("DELETE FROM ingredients WHERE name = ?", (name,))
    conn.commit()
    conn.close()

