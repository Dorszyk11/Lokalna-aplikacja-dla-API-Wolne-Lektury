from .models import db, Book, Epoch, Genre, Kind, Author

def add_book(data):
    book = Book(
        title=data['title'],
        epoch_id=data['epoch_id'],
        genre_id=data['genre_id'],
        kind_id=data['kind_id'],
        author_id=data['author_id']
    )
    db.session.add(book)
    db.session.commit()
    return book

def add_categories(data):
    for category_type, categories in data.items():
        for category in categories:
            if category_type == 'epochs':
                db.session.add(Epoch(name=category['name']))
            elif category_type == 'genres':
                db.session.add(Genre(name=category['name']))
            elif category_type == 'kinds':
                db.session.add(Kind(name=category['name']))
            elif category_type == 'authors':
                db.session.add(Author(name=category['name']))
    db.session.commit()
    return data

def filter_books(filters):
    query = Book.query
    if 'epoch' in filters:
        query = query.filter(Book.epoch.has(name=filters['epoch']))
    if 'genre' in filters:
        query = query.filter(Book.genre.has(name=filters['genre']))
    if 'kind' in filters:
        query = query.filter(Book.kind.has(name=filters['kind']))
    if 'author' in filters:
        query = query.filter(Book.author.has(name=filters['author']))
    return query.all()
