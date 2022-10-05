from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fproject'
mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
        nombre_tarea = request.form['nombre_tarea']
        desc_tarea = request.form['desc_tarea']
        dia_tarea= request.form['dia_tarea']
        estado_tarea = request.form['estado_tarea']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tareas (nombre_tarea, desc_tarea, dia_tarea, estado_tarea) VALUES (%s, %s, %s, %s)',
        (nombre_tarea, desc_tarea, dia_tarea, estado_tarea))
        mysql.connection.commit()
        flash('Recibido correctamente')
        return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == '__main__':
 app.run(port = 5000, debug = True)

