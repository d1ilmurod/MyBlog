from django.urls import path
from .views import HomePage,profile_page,books_page,books_detail_page


urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('profile/<int:pk>/',profile_page,name='profile_detail'),
    path('books/',books_page,name='books_page'),
    path('books/<int:pk>/',books_detail_page,name='books_detail'),
]