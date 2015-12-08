from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urls = []
urls.append(url(r'^hello/$', 'index', {}))
urlpatterns = patterns('blog.views', *urls)