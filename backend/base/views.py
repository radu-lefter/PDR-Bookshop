from django.shortcuts import render
from django.http import JsonResponse
from .books import books
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'api/books', 
        'api/books/create'
    ]
    return Response(routes)

@api_view(['GET'])
def getBooks(request):
    return Response(books)

@api_view(['GET'])
def getBook(request, bk):
    book = None
    for i in books:
        if i['_id'] == bk:
            book = i
            break
    return Response(book)