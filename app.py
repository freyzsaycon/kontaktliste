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

# Hashe passordet med hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Verifisere det hashende passordet
def verify_password(stored_password, password_to_check):
    return stored_password == hashlib.sha256(password_to_check.encode()).hexdigest()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        brukernavn = request.form['username']
        passord = request.form['password']
        passord_hash = hash_password(passord)

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (brukernavn,))
        bruker = cursor.fetchone()
        conn.close()

        if bruker and bruker['password'] == passord_hash:
            session['user'] = brukernavn
            return redirect('/dashboard')
        else:
            return 'Feil brukernavn eller passord'

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        brukernavn = request.form['username']
        passord = request.form['password']
        passord_hash = hash_password(passord)

        conn = get_db_connection()
        cursor = conn.cursor()
    
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (brukernavn, passord_hash))
        conn.commit()
        return "Bruker registrert!"
            
    return render_template('register.html')



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
