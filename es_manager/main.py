from es_manager import app
from flask import render_template, request, redirect, url_for, flash, session
import sqlite3
import re

DATABASE = 'database.db'

@app.route('/')
def index():
  con = sqlite3.connect(DATABASE)
  db_books = con.execute("select * from books").fetchall()
  con.close()

  books = []
  for row in db_books:
    books.append(
      {
        'title': row[1],
        'price': row[2],
        'arrival_day': row[3],
        'id': row[0]
      }
    )

  return render_template(
    'index.html',
    books = books,
    )


@app.route('/form')
def form():
  return render_template(
    'form.html'
  )


@app.route('/register', methods=['POST'])
def register():
  # validation
  if not re.match(r'^[0-9]+$', request.form['price']):
    flash("金額には半角で自然数を入力してください")
    return render_template(
      'form.html',
      title=request.form['title'],
      price=request.form['price'],
      arrival_day=request.form['arrival_day']
    )

  # registration to db
  con = sqlite3.connect(DATABASE)
  con.execute('insert into books (title, price, arrival_day) values (?, ?, ?)',
              [request.form['title'], request.form['price'], request.form['arrival_day']])
  con.commit()
  con.close()
  flash("追加しました")

  return redirect(url_for('index'))


@app.route('/edit/<int:id>')
def edit(id):
  con = sqlite3.connect(DATABASE)
  record = con.execute('select * from books where id=?', [id]).fetchall()[0]
  con.close()

  return render_template(
    'edit.html',
    id=record[0],
    title=record[1],
    price=record[2],
    arrival_day=record[3]
  )


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
  con = sqlite3.connect(DATABASE)
  con.execute('update books set title=?, price=?, arrival_day=? where id=?',
              [request.form['title'], request.form['price'], request.form['arrival_day'], id])
  con.commit()
  con.close()
  flash("変更しました")

  return redirect('/')


@app.route('/delete/<int:id>', methods=["POST"])
def delete(id):
  con = sqlite3.connect(DATABASE)
  con.execute('delete from books where id=?',[id])
  con.commit()
  con.close()
  flash("削除しました")

  return redirect('/')
