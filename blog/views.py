from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from . models import MyBlog, Tag


def index(request):
	return render(request, 'blog/index.html')

def blogs(request):
	lis = MyBlog.objects.order_by('title')
	con = {'lis' : lis}
	return render(request,'blog/blogs.html', con)

def about(request):
	return render(request,'blog/about.html')

def blog_details2(request, blog_id):
	try:
		blog = MyBlog.objects.get(pk=blog_id)
	except MyBlog.DoesNotExist:
		raise Http404("Blog does not exist")
	return render(request,'blog/blog-details2.html', {'blog' : blog})