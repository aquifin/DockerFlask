from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__,template_folder='templates')
	

def create_database():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students ( id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL)''')
    conn.commit()
    conn.close()
	
	
@app.route('/')
def index():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    students = c.fetchall()
    conn.close()
    return render_template('index.html', rows=students)

@app.route('/add', methods=['POST'])
def add_task():
    name = request.form['name']
    age = request.form['age']
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('INSERT INTO students (name,age) VALUES (?,?)', (name,age))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
	
	
if __name__ == "__main__":
    create_database()
    app.run(debug=True)