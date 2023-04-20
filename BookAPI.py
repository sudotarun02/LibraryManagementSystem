from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(200))
    available = db.Column(db.Boolean, default=True)

    def __init__(self, title, author):
        self.title = title
        self.author = author


# Login test
'''
@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        return jsonify({'message': 'Login Successful'})

    return jsonify({'message': 'Could not Authenticate'}), 404
    '''


# Welcome route

@app.route('/')
def welcome():
    return 'home'


# Add books

@app.route('/books', methods=['POST'])
def add_book():
    with app.app_context():
        title = request.json['title']
        author = request.json['author']
        new_book = Book(title=title, author=author)

        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully'})


# Retrieve all books

@app.route('/books', methods=['GET'])
def view():
    books = Book.query.all()
    book_list = [{'id': book.id, 'title': book.title, 'author': book.author}
                 for book in books]
    return jsonify({'Books': book_list})


# Delete books by id

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    with app.app_context():
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return jsonify({'message': f'Book with ID {book_id} deleted successfully'})
        else:
            return jsonify({'message': f'Book with ID {book_id} not found'}), 404


# Retrieve books by id

@app.route('/books/<int:book_id>', methods=['GET'])
def bookid(book_id):
    with app.app_context():
        book = Book.query.get(book_id)
        if book:
            return jsonify({'id': book.id, 'title': book.title, 'author': book.author})
        else:
            return jsonify({'message': f'Book with ID {book_id} not found'}), 404


# Update books by id

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    # Update book data based on request body

    title = request.json.get('title')
    author = request.json.get('author')
    if title:
        book.title = title
    if author:
        book.author = author

    db.session.commit()

    return jsonify({'id': book.id, 'title': book.title, 'author': book.author})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
