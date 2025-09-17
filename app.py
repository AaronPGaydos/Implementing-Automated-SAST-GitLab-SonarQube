# intentionally insecure
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/login")
def login():
    user = request.args.get("user")
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE name='{user}'"  # SQL Injection risk
    conn.execute(query)
    return f"Welcome {user}!"
