"""Django URL Configuration

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
from django.conf.urls import url, include    # Notice we added include
from django.contrib import admin 

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^Django/', include('apps.first_app.urls')),    #and now we use the include function to pull in our first_app.urls...
    url(r'^blogs_app/', include('apps.blogs_app.urls')),
    # url(r'^Django/', include('apps.surveys_app.urls')),
]