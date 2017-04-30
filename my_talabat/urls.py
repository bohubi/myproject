from django.conf.urls import url

from my_talabat import views

urlpatterns = [

    url(r'^$', views.fat_locations),

    url(r'^(?P<restaurant_id>[0-9]+)/$', views.res_cat),

    url(r'^(?P<cat_id>[0-9]+)/items/$', views.items),

]
