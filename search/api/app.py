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
    try:
        conn = get_db_connection()
        arrays = conn.execute('SELECT * FROM arrays').fetchall()
        conn.close()
        return render_template('index.html', arrays=arrays)
    except Exception as error:
        raise 
        abort(500)


@app.route('/<int:array_id>', methods=('GET', 'POST'))
def array(array_id):
    array = get_array(array_id) 
    target_pos = 0
    try:
        if request.method == 'POST':
            target = int(request.form['target'])
            #print(target)
            nums=[int(item) for item in array['content'].split()]
            sol = Solution()
            target_pos = sol.search(nums, target)
            
    except Exception as error:
        flash(repr(error))
        print('An exception occurred: {}'.format(error.with_traceback))
        raise 
        abort(500)
        raise
    return render_template('array.html', array=array, target_pos = target_pos)
        #logging.error(traceback.format_exc())
        
    


@app.route('/create', methods=('GET', 'POST'))
def create():
    try:
        if request.method == 'POST':
            #print(request.form['title'])
            title = request.form['title']
            content = request.form['content']

            if not title:
                flash('Title is required!')
            elif not content:
                flash('Content is required!')
            else:
                nums = []
                for num in content.split():
                    try:
                        a = int(num)
                    except TypeError as error:
                        raise 
                    nums.append(a)

                if all(nums[i] <= nums[i+1] for i in range(nums.index(min(nums)) - 1)) != True or  all(nums[j] <= nums[j+1] for j in range(nums.index(min(nums)), len(nums)-1)) != True:
                    raise ValueError

                if len(nums) < 1 :
                    raise ValueError
                
                if  len(nums) > 5000:
                    raise ValueError

                if max(nums) > 10000 or min(nums) < -10000:
                    raise ValueError
                
                if len(nums) != len(set(nums)):
                    raise ValueError
                
                conn = get_db_connection()
                conn.execute('INSERT INTO arrays (title, content) VALUES (?, ?)',
                            (title, content))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))
    except  Exception as error:
        flash(repr(error))
        print('An exception occurred: {}'.format(error.with_traceback))
        #logging.error(traceback.format_exc())
        raise 
        abort(500)
        #raise

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    try:
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
    except  Exception  as error:
        flash(repr(error))
        print('An exception occurred: {}'.format(error.with_traceback))
        #logging.error(traceback.format_exc())
        raise 
        abort(500)
        raise 

    return render_template('edit.html', array=array)



@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    try:
        array = get_array(id)
        conn = get_db_connection()
        conn.execute('DELETE FROM arrays WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        flash('"{}" was successfully deleted!'.format(array['title']))
    except  Exception  as error:
        flash(repr(error))
        print('An exception occurred: {}'.format(error.with_traceback))
        abort(500)
        raise error
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