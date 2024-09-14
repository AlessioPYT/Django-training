from pymongo import MongoClient
from django.contrib.auth.models import User
from quotes.models import Author, Quote

def migrate_data():
    client = MongoClient('mongodb://localhost:27017/')
    mongo_db = client['mongo_db']

    for author in mongo_db.authors.find():
        Author.objects.create(
            name=author['name'],
            birthdate=author.get('birthdate'),
            bio=author['bio']
        )

    for quote in mongo_db.quotes.find():
        author = Author.objects.get(name=quote['author'])
        Quote.objects.create(
            text=quote['text'],
            author=author,
            tags=','.join(quote['tags'])
        )
