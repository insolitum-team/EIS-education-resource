from django.shortcuts import render
from .models import PostModel
from .date_functions import YEAR


def index(request):
	posts = PostModel.objects.all().order_by('-date')
	return render(request, 'eis/index.html', {
		'year': YEAR,
		'posts': posts,
	})


def post(request, post_id):
	current_post = PostModel.objects.get(pk=post_id)
	return render(request, 'eis/post.html', {
		'year': YEAR,
		'post': current_post
	})


def search(request):
	if request.method == 'POST':
		search_request = request.POST['search']
		searched_posts = PostModel.objects.filter(body__contains=search_request)
		return render(request, 'eis/search.html', {'year': YEAR, 'posts': searched_posts})
