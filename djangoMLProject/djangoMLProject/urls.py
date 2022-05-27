"""djangoMLProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

import ML.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ML.views.start),
    path('ML/', ML.views.index),
    path('ML/insert', ML.views.insert),
    path('ML/insert2', ML.views.insert2),
    path('ML/one', ML.views.one),
    path('ML/one2', ML.views.one2),
    path('ML/output/<id>', ML.views.output),
    path('ML/chart', ML.views.chart),
    path('ML/chart2', ML.views.chart2)

]
