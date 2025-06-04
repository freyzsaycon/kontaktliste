from flask import Flask, render_template, request, redirect, session
import mysql.connector
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")  # For session

# Koble til database
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
