from django.conf.urls import patterns, include, url
from django.contrib import admin
# from inventory.models import games
from inventory import views

urlpatterns = patterns(
  '',
  url(r'^$', views.index, name='index'),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^game/(?P<game_id>\d+)/$$', views.detail, name='detail'),
  url(r'^game/new/$$', views.new, name='new'),
)
