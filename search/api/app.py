import sqlite3
import traceback
import logging
from solution import Solution
from flask import Flask, render_template, request, url_for, flash, redirect
'''Глобальный объект request для доступа к входящим данным запроса, которые будут подаваться через форму HTML.
Функция url_for() для генерирования URL-адресов.
Функция flash() для появления сообщения при обработке запроса.
Функция redirect() для перенаправления клиента в другое расположение.'''
from werkzeug.exceptions import abort #Для ответа в виде страницы 404

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_array(array_id):
    conn = get_db_connection()
    array = conn.execute('SELECT * FROM arrays WHERE id = ?',
                        (array_id,)).fetchone()
    conn.close()
    #if array is None:
    #    abort(404)
    return array

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SSSEKRRET1234KEY'


@app.route('/')
def index():
    conn = get_db_connection()
    arrays = conn.execute('SELECT * FROM arrays').fetchall()
    conn.close()
    return render_template('index.html', arrays=arrays)


@app.route('/<int:array_id>', methods=('GET', 'POST'))
def array(array_id):
    array = get_array(array_id)
    target_pos = 0
    try:
        if request.method == 'POST':
            target = int(request.form['target'])
            nums=[int(item) for item in array['content'].split()]
            sol = Solution()
            target_pos = sol.search(nums, target)
    except  BaseException as error:
        print('An exception occurred: {}'.format(error.with_traceback))
        #logging.error(traceback.format_exc())
        
    return render_template('array.html', array=array, target_pos = target_pos)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO arrays (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    array = get_array(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE arrays SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            array = get_array(id)
            return render_template('array.html', array=array)

    return render_template('edit.html', array=array)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    array = get_array(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM arrays WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(array['title']))
    return redirect(url_for('index'))




"""@app.route('/solution')
def solution(id):
    array = get_array(id)
    conn = get_db_connection()
    arrays = conn.execute('SELECT * FROM arrays').fetchall()
    conn.close()
    nums=[int(item) for item in "1 2 3".split()]
    target = 2
    sol = Solution()
    target_pos = sol.search(nums, target)
    print(target_pos)
    return render_template('array.html', array=array, target_pos = target_pos)"""

if __name__ == '__main__':
    app.run(debug=True)

'''a = "4,5,6,7,0,1,2".split(",")
a = [int(item) for item in a]

print(list(range(10, 5001+1))+list(range(1, 10)))
s = Solution()
print(s.search(list(range(10, 5001+1))+list(range(1, 10)), 100))'''