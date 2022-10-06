from flask import Flask
app = Flask(__name__)
app.secret_key = b'ftuajii'
import test.main

from test import db
db.create_books_table()
