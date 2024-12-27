from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView

def recipe_recipe(request):
    recipe = Articles.objects.filter(dish='Первое')
    return render(request, 'recipe/recipe_lok.html', {'recipe': recipe})

def recipe_two(request):
    recipe = Articles.objects.filter(dish='Второе')
    return render(request, 'recipe/recipe_two_Russia.html', {'recipe': recipe})

def recipe_marinade(request):
    recipe = Articles.objects.filter(dish='Маринад')
    return render(request, 'recipe/recipe_marinade_Russia.html', {'recipe': recipe})

def recipe_seasonings(request):
    recipe = Articles.objects.filter(dish='Приправа')
    return render(request, 'recipe/recipe_seasonings_Russia.html', {'recipe': recipe})

def recipe_snacks(request):
    recipe = Articles.objects.filter(dish='Закуска')
    return render(request, 'recipe/recipe_snacks_Russia.html', {'recipe': recipe})

def recipe_desserts(request):
    recipe = Articles.objects.filter(dish='Десерт')
    return render(request, 'recipe/recipe_desserts_Russia.html', {'recipe': recipe})

def recipe_registration(request):
    recipe = Articles.objects.filter(dish='Десерт')
    return render(request, 'recipe/recipe_registration.html', {'recipe': recipe})

class RecipeDetailView(DetailView):
    model = Articles
    template_name = "recipe/recipe_view.html"
    context_object_name = 'article'

def addrecipe(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверно заполнена'

    form = ArticlesForm()
        
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'recipe/recipe_create.html', data)