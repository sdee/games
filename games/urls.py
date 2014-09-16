from django.conf.urls import patterns, include, url
from django.contrib import admin
# from inventory.models import games
from inventory import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'games.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^game/(?P<game_id>\d+)/$$', views.detail, name='detail'),
    url(r'^game/new/$$', views.new, name='new'),
)
