from django.shortcuts import render
import datetime


def index(request):
	year = datetime.date.today().year
	return render(request, 'eis/index.html', {'year': year})
