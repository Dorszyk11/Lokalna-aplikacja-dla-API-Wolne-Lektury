from flask import request, jsonify
from . import db
from .models import Book, Epoch, Genre, Kind, Author
from .services import add_book, add_categories, filter_books

def init_routes(app):
    @app.route('/books', methods=['POST'])
    def create_book():
        data = request.json
        book = add_book(data)
        return jsonify(book), 201

    @app.route('/categories', methods=['POST'])
    def create_categories():
        data = request.json
        categories = add_categories(data)
        return jsonify(categories), 201

    @app.route('/books', methods=['GET'])
    def get_books():
        filters = request.args
        books = filter_books(filters)
        return jsonify(books), 200
