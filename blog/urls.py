from django.conf.urls import url, patterns
from . import views

# urlpatterns =[
#    url(r'^$', views.index, name = 'index')
#    url(r'^blogs/$', 'blogs.views.blogs', name = 'blogs')
#    # url(r'^about/$', views.about, name = 'about')

# ]  

urlpatterns = patterns('blog.views',
	url(r'^$', 'index', name='index'),
    url(r'^blogs/', 'blogs', name='blogs'),
    url(r'^about/', 'about', name='about' ),
    # url(r'^blog-details2/', 'blog_details2', name='blog-details2'),
    url(r'^(?P<blog_id>[0-9]+)/$', 'blog_details2', name='blog-details2'),

	)
