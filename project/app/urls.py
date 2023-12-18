from django.urls import path
from .views import news_add, edit_news, delete_news, get_news

urlpatterns = [
    path('news/', get_news, name='news_list'),
    path('news/add', news_add, name='news_add'),
    path('news/edit/<int:news_id>', edit_news, name='edit_news'),
    path('news/delete/<int:news_id>', delete_news, name='delete_news'),
]
