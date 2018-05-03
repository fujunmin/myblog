"""myblog URL Configuration

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
import sys
import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print BASE_DIR
# sys.path.append(BASE_DIR)
# reload(sys)
from django.conf.urls import url,include
from django.contrib import admin
import blog.views as bv


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^index/', bv.index),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('blog.urls',namespace='blog')),


]
