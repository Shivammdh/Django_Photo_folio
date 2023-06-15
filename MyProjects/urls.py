"""MyProjects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from MyProjects import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about-us/',views.aboutus,name='about-us'),
    # path('.*/<str:contact>',views.contact,name='contact'),
    path('contact/',views.contact,name='contact-us'),
    path('services/',views.services,name='our-services'),
    path('gallery-page/',views.gallery,name='gallery'),
    path('gallerysingle/',views.gallerysingle,name='gallerysingle'),
    path('course/<str:timeframe>', views.goals_by_timeframe,name='goals'),
    path('userformget/',views.userformGet,name='userformget'),
    path('userformpost/',views.userformPost,name='userformpost'),
    path('djangoInputForm/',views.djangoInputForm,name='djangoInputForm'),
    path('success/',views.success,name='success'),
    path('calculator/',views.calculator,name='calculator'),
    path('evenodd/',views.evenodd,name='evenodd'),
    path('marksheet/',views.marksheet,name='marksheet'),
    path('evenoddblankinput/',views.evenoddblankinput,name='evenoddblankinput'),
    path('newsdetail/<newsid>',views.news_details,name='news_detail'),
    path('userinfo/',views.user_information,name='userinfo'),
    # path('yourmarksheet',views.yourmarksheet,name='yourmarksheet'),

]
