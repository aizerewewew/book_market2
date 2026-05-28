from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Деректер базасын инициализациялау
def init_db():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books 
                      (id INTEGER PRIMARY KEY, title TEXT, price TEXT, 
                       university TEXT, location TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form.get('title')
    price = request.form.get('price')
    uni = request.form.get('university')
    loc = request.form.get('location')
    
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, price, university, location) VALUES (?, ?, ?, ?)", 
                   (title, price, uni, loc))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    # app.py-дағы add_book функциясын осылай жаңартыңыз
@app.route('/add', methods=['POST'])
def add_book():
    title = request.form.get('title')
    price = request.form.get('price')
    uni = request.form.get('university')
    loc = request.form.get('location')
    phone = request.form.get('phone') # Жаңа өріс
    
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    # Жаңа колонканы SQL-ге қостық
    cursor.execute("INSERT INTO books (title, price, university, location, phone) VALUES (?, ?, ?, ?, ?)", 
                   (title, price, uni, loc, phone))
    conn.commit()
    conn.close()
    return redirect('/')