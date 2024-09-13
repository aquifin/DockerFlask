from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app_flask = Flask(__name__,template_folder='templates')
	

def connect_db():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    
    return conn,c
    
def create_database():
    conn,c = connect_db()
    c.execute('''CREATE TABLE IF NOT EXISTS students ( id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL)''')
    conn.commit()
    conn.close()
	
	
@app_flask.route('/')
def landingpage():
    conn,c = connect_db()
    c.execute('SELECT * FROM students')
    students = c.fetchall()
    conn.close()
    return render_template('index.html', rows=students)

@app_flask.route('/add', methods=['POST'])
def add_task():
    name = request.form['name']
    age = request.form['age']
    
    conn,c = connect_db()
    c.execute('INSERT INTO students (name,age) VALUES (?,?)', (name,age))
    conn.commit()
    conn.close()
    return redirect(url_for('landingpage'))

@app_flask.route('/delete/<int:id>')
def delete_task(id):
    conn,c = connect_db()
    c.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('landingpage'))
	
	
if __name__ == "__main__":
    create_database()
    app_flask.run(debug=True,host='0.0.0.0', port=5000)