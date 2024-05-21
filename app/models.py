from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    epoch_id = db.Column(db.Integer, db.ForeignKey('epoch.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    kind_id = db.Column(db.Integer, db.ForeignKey('kind.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

class Epoch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    books = db.relationship('Book', backref='epoch', lazy=True)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    books = db.relationship('Book', backref='genre', lazy=True)

class Kind(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    books = db.relationship('Book', backref='kind', lazy=True)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)
