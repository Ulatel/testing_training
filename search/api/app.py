import sqlite3
import unittest
import logging
from api.solution import Solution
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
    print(array_id)
    array = conn.execute('SELECT * FROM arrays WHERE id = "'+str(array_id)+'"').fetchone()
    conn.close()
    #if array is None:
    #    abort(404)
    return array

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SSSEKRRET1234KEY'


@app.route('/', methods=('GET', 'POST'))
def index():

        conn = get_db_connection()
        if request.method == 'POST':
            year = "2024-01-01 10:16:"+str(request.form['year'])
            print(year)
            arrays = conn.execute("SELECT * FROM arrays WHERE created<'"+year+"' AND title NOT LIKE '%Flag%'",
                        ).fetchall()
        else:
            arrays = conn.execute("SELECT * FROM arrays WHERE  title NOT LIKE '%Flag%'").fetchall()
        conn.close()
        return render_template('index.html', arrays=arrays)
    


@app.route('/<array_id>', methods=('GET', 'POST'))
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
            elif not content :
                flash('Content is required!')
            else:
                if len(content.split())<1:
                    flash('Надо не пустую!')
                    #raise ValueError
                nums = []
                for num in content.split():
                    try:
                        a = int(num)
                    except TypeError as error:
                        flash('не число....!')
                        raise 
                    nums.append(a)

                if all(nums[i] <= nums[i+1] for i in range(nums.index(min(nums)) - 1)) != True or  all(nums[j] <= nums[j+1] for j in range(nums.index(min(nums)), len(nums)-1)) != True:
                    
                    flash('не сортировано...!')
                    #raise ValueError

                elif len(nums) < 1 :
                    flash('не пустую...!')
                    #raise ValueError
                
                elif  len(nums) > 5000:
                    flash('сильно длинно!')
                    #raise ValueError

                elif max(nums) > 10000 or min(nums) < -10000:
                    flash('плохие значения!')
                    #raise ValueError
                
                elif len(nums) != len(set(nums)):
                    flash('надо шоб уникально в числах было...!')
                    #raise ValueError
                
                else:
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
            elif not content :
                flash('Content is required!')
            else:
                if len(content.split())<1:
                    flash('Надо не пустую!')
                    #raise ValueError
                nums = []
                for num in content.split():
                    try:
                        a = int(num)
                    except TypeError as error:
                        flash('не число....!')
                        raise 
                    nums.append(a)

                if all(nums[i] <= nums[i+1] for i in range(nums.index(min(nums)) - 1)) != True or  all(nums[j] <= nums[j+1] for j in range(nums.index(min(nums)), len(nums)-1)) != True:
                    
                    flash('не сортировано...!')
                    #raise ValueError

                elif len(nums) < 1 :
                    flash('не пустую...!')
                    #raise ValueError
                
                elif  len(nums) > 5000:
                    flash('сильно длинно!')
                    #raise ValueError

                elif max(nums) > 10000 or min(nums) < -10000:
                    flash('плохие значения!')
                    #raise ValueError
                
                elif len(nums) != len(set(nums)):
                    flash('надо шоб уникально в числах было...!')
                    #raise ValueError
                
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
        raise 
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