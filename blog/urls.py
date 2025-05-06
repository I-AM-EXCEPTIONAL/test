from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post,category,year , search_results , about_us,contact, desclaimer, privacy, terms
urlpatterns = [
    path('', home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category),
    path('year/<slug:url>', year),
    path('search_url', search_results),
    path('about_us', about_us),
    path('contact', contact),
    path('desclaimer',desclaimer ),
    path('privacy', privacy),
    path('terms', terms),


    
]