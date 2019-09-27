"""transport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

react_routes = getattr(settings, 'REACT_ROUTES', [])
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('transdb.urls')),
    path('',views.ReactAppView.as_view()),
    path('<slug:slug>',views.ReactAppView.as_view()),
    path('favicon.ico',views.FaviconView.as_view()),
    path('manifest.json',views.ManifestView.as_view()),
    path('service-worker.js',views.ServiceWorkerView.as_view()),
]
for route in react_routes:
    urlpatterns += [
        path('<slug:slug>'+'{}'.format(route),views.ReactAppView.as_view())
    ]

from transdb.models import CollegeList
for x in CollegeList.objects.all():
    urlpatterns += [
        path('<slug:slug>'+'/{}'.format(x.collegeURL),views.ReactAppView.as_view())
    ]