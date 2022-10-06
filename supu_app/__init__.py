from flask import Flask
app = Flask(__name__)
app.secret_key = b'ftuajii'
import supu_app.main

from supu_app import db
db.create_books_table()
