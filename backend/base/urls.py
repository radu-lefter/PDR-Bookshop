from django.urls import path
from . import views


urlpatterns = [
    path('users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.getRoutes, name='routes'),
    path('books/', views.getBooks, name='books'),
    path('books/<str:pk>/', views.getBook, name='book'),
]
