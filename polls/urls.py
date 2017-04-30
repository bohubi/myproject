from django.conf.urls import url

from . import views
app_name= "polls"

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^question/(?P<question_id>[0-9]+)/results/$', views.todo, name='results'),
    url(r'^question/(?P<question_id>[0-9]+)/edit/$', views.edit_question, name="edit"),
    url(r'^question/(?P<question_id>[0-9]+)/update/$', views.todo),
    url(r'^question/(?P<question_id>[0-9]+)/delete/$', views.delete_question , name="delete_question"),
    url(r'^question/new/$', views.add_question, name="add_question"),
    url(r'^question/choice/new/$', views.add_choice, name='add_choice'),
    url(r'^question/(?P<choice_id>[0-9]+)/edit_choice/$', views.edit_choice, name="edit_choice"),
    url(r'^question/(?P<choice_id>[0-9]+)/delete_choice/$', views.delete_choice, name="delete_choice"),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^use_api$', views.use_api, name='use_api'),
    url(r'^use_api2', views.use_api2, name='use_api2'),
    url(r'^maps', views.maps, name='maps'),
#     url(r'^question/create/$',views.todo),
#     url(r'^choice/(?P<choice_id>[0-9]+)/edit/$', views.todo),
#     url(r'^choice/(?P<choice_id>[0-9]+)/update/$', views.todo),
#     url(r'^choice/(?P<choice_id>[0-9]+)/delete/$', views.todo),
#     url(r'^choice/new/$', views.todo),
#     url(r'^choice/create/$',views.todo),
    ]


    # url(r'^question/(?P<question_id>[0-9]+)/results/$', views.detail, name='results'),
""""# ex: /polls/5/
   url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
   # ex: /polls/5/results/
   url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
   # ex: /polls/5/vote/

   url(r"^check/(?P<stuff>[a-zA-Z0-9]+)/(?P<more>[0-9]+)/(?P<araboo>.+)$", views.itworks),"""