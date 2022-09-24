from django.contrib import admin
from .models import PostModel


@admin.register(PostModel)
class Post(admin.ModelAdmin):
	list_display = (
		'title',
		'date',
	)
	ordering = ('-date',)
