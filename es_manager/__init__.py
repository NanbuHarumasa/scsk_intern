from flask import Flask
app = Flask(__name__)
app.secret_key = b'ftuajii'
import es_manager.main

from es_manager import db
db.create_books_table()
