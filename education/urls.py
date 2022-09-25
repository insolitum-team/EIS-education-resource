from django.urls import path
from .views import index, post, search

urlpatterns = [
	path('', index, name='index'),
	path('post/<post_id>', post, name='post'),
	path('search', search, name='search')
]
