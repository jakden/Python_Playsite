from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hearthstone/', include('hearthstone.urls', namespace="hearthstone")),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
	
]

