from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('top_Russia', views.recipe_recipe, ),
    path('two_Russia', views.recipe_two, ),
    path('marinade_Russia', views.recipe_marinade, ),
    path('seasonings_Russia', views.recipe_seasonings, ),
    path('registration', views.recipe_registration, ),
    path('snacks_Russia', views.recipe_snacks, ),
    path('desserts_Russia', views.recipe_desserts, ),
    path('addarecipe', views.addrecipe ),
    path('<int:pk>', views.RecipeDetailView.as_view(), name = 'recipe-detail' )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)