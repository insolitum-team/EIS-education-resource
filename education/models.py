from django.db import models
from ckeditor.fields import RichTextField


class PostModel(models.Model):
	title = models.CharField('Заголовок', max_length=100)
	subtitle = models.CharField('Подзаголовок', max_length=255)
	body = RichTextField()
	date = models.DateTimeField('Дата', auto_now_add=True)

	def __str__(self):
		return self.title
