from django.forms import ModelForm
from django import forms
from .models import PostModel
from ckeditor.widgets import CKEditorWidget


class PostModelForm(ModelForm):
	class Meta:
		model = PostModel
		fields = ('title', 'subtitle', 'body')
		labels = {
			'title': 'Заголовок',
			'subtitle': 'Подзаголовок',
			'body': 'Основной текст',
		}
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.CharField(widget=CKEditorWidget()),
		}
