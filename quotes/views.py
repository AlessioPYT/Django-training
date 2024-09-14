from django.shortcuts import render
from .models import Author, Quote

def quotes_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quotes_list.html', {'quotes': quotes})

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})
