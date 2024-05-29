import sqlite3

db = sqlite3.connect('books_database.db')
cursor = db.cursor()
# Creating a table
cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(250) NOT NULL "
               "UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

book_title = input('Enter book title: ')
book_author = input('Enter book author: ')
book_rating = float(input('Enter book rating: '))

cursor.execute("INSERT INTO books (title, author, rating) VALUES (?, ?, ?)",
               (book_title, book_author, book_rating))

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
