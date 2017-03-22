from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^hello/$', views.fat_locations),

    url(r'^(?P<restaurant_id>[0-9]+)/$', views.res_cat),

    url(r'^(?P<cat_id>[0-9]+)/items/$', views.items),

]
