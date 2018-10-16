from django.contrib import admin
from django.urls import re_path,include
from . import views
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns
urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^articles/',include('articles.urls')),
    re_path(r'^about/$', views.about),
]

urlpatterns += staticfiles_urlpatterns()