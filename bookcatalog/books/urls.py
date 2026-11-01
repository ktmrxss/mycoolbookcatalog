from django.urls import path
from . import views  # Импортируем views из текущего приложения

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Главная страница со списком книг
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),  # URL для просмотра конкретной книги по ID
    path('search/', views.search_books, name='search')  # URL для страницы поиска книг
]
