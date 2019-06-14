"""projectX5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.companylist.as_view(),name="company"),
    url(r'^(?P<pk>\d+)/$', views.companydetail.as_view(),name="detail"),
    url(r'^update/(?P<pk>\d+)/$', views.companyupdateview.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', views.companydeleteview.as_view()),
    url(r'^create/', views.companycreateview.as_view()),
]
