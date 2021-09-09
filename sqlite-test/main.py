import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), unique=True, nullable=False)
    author = db.Column(db.String(30), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


db.create_all()

new_book = Book(id=1, title='SOLYARA', author='Arthas', rating=7.4)
#db.session.add(new_book)
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()

# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(10, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
