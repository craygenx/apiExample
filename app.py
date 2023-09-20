from flask import Flask, jsonify, make_response, request
from models.Book import db, Book
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Books library API'

@app.route('/books', methods=['GET'])
def Books():
    books = []
    for book in Book.query.all():
        book_dict = {
            'id': book.id,
            'title': book.title,
            'author': book.authur
        }
        books.append(book_dict)
    response = make_response(
        jsonify(books),
        200
    )
    return response

@app.route('/book/<int:id>', methods=['GET', 'PUT'])
def book(id):
    if request.method == 'GET':
        book = Book.query.filter_by(id=id).first()
        if book:
            book_dict = {
                'id': book.id,
                'title': book.title,
                'author': book.authur
            }
            response = make_response(
                jsonify(book_dict),
                200
            )
            response.headers['Content-Type']='application/json'
            return response
    else:
        book = Book.query.get(id)
        if not book:
            return jsonify({'error': 'Book not found'})
        data = request.get_json()
        book.title = data['title']
        book.authur = data['author']
        db.session.commit()
        return jsonify({'message': 'Book updated succesfully'})

@app.route('/update', methods=['POST'])
def submit_book():
    data = request.get_json()
    new_book = Book(title=data['title'], authur=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book submitted'})

db.init_app(app)
if __name__ == '__main__':
    app.run(port=5555)