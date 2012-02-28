from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello Dotcloud!")

def home(request):
	return HttpResponse("Hello HaiTaoKong!")

