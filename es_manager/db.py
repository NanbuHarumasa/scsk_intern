import sqlite3

DATABASE = 'database.db'

def create_books_table():
  con = sqlite3.connect(DATABASE)
  con.execute("create table if not exists books \
    (id integer primary key autoincrement,\
      title text, price integer, arrival_day text)")
  con.close()
