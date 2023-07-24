#from django.views.generic.detail import DetailView
#from django.views.generic.list import ListView
#from .models import Author, Book

#class BookListView(ListView):
#    model = Book
 #   template_name = "book_list.html"

#class BookDetailView(DetailView):
 #   model = Book
  #  template_name = "book_detail.html"

from django.http import JsonResponse
from .models import Book, Author

def book_list(request):
    print('Request를 받았다')
    books = Book.objects.all() #Book object를 다 가져온다
    data = {"books": list(books.values())}
    response = JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    return response

def book_detail(request, pk):
    book = Book.objects.get(pk=pk) # 특정 Book object를 가져온다
    data = {
        "book": {
            "author": book.author.name,
            "name": book.name,
            "description": book.description,
            "shipping_cost": book.shipping_cost,
            "quantity": book.quantity
        }
    }

    response = JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    return response
    
 