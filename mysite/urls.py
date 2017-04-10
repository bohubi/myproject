from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^my_talabat/', include('my_talabat.urls')),
    url(r'^tvguide/', include('tvguide.urls')),
]
