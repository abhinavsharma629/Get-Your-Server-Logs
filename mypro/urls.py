from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from webap import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('process', views.processList.as_view()),
    path('stat', views.statList.as_view()),
]
#binds functions to methods as_view()
#get ka get , post ko post method etc
urlpatterns=format_suffix_patterns(urlpatterns)