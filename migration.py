from quotes.models import Author, Quote
from pymongo import MongoClient

def migrate_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_mongodb_name']

    
    authors = db.authors.find()
    for author in authors:
        Author.objects.create(name=author['name'], bio=author['bio'])

    
    quotes = db.quotes.find()
    for quote in quotes:
        author = Author.objects.get(name=quote['author_name'])
        Quote.objects.create(text=quote['text'], author=author)

if __name__ == '__main__':
    migrate_data()
