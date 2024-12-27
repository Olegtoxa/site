from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home' ),
    path('addarecipe', views.addarecipe ),
    path('recipe', views.recipe ),
    path('kitchens', views.kitchens, name = 'kitchens' ),
    path('kitchenstransition', views.kitchenstransition ),
    path('likes', views.likes ),
    path('notlikes', views.notlikes, name = 'notlikes' ),
    path('registration', views.registration, name='reg' ),
    path('one_Russia', views.one_Russia ),
    path('two_Russia', views.two_Russia ),
    path('top_Russia', views.top_Russia ),
    path('marinade_Russia', views.marinade_Russia ),
    path('seasonings_Russia', views.seasonings_Russia ),
    path('snacks_Russia', views.snacks_Russia ),
    path('desserts_Russia', views.desserts_Russia ),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

