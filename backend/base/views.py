from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .books import books
from .models  import Book
from .serializers import BookSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyMyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        #Add custom claims
        data['username'] = self.user.username
        data['email'] = self.user.email

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyMyTokenObtainPairSerializer


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
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(_id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)