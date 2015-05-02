from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'pokepy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pokepy.views.index', name = 'index'),
    url(r'^search/', 'pokepy.views.search', name = 'search'),
    url(r'^search_result/', 'pokepy.views.search_result' , name='search_result'),
]
