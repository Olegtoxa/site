from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def addarecipe(request):
    return render(request, "main/addarecipe.html")

def recipe(request):
    return render(request, "main/recipe.html")

def kitchens(request):
    return render(request, "main/kitchens.html")

def kitchenstransition(request):
    return render(request, "main/kitchenstransition.html")

def likes(request):
    return render(request, "main/likes.html")

def notlikes(request):
    return render(request, "main/notlikes.html")

def registration(request):
    return render(request, "main/registration.html")

def one_Russia(request):
    return render(request, "main/one_Russia.html")

def top_Russia(request):
    return render(request, "main/top_Russia.html")

def two_Russia(request):
    return render(request, "main/two_Russia.html")

def marinade_Russia(request):
    return render(request, "main/marinade_Russia.html")

def seasonings_Russia(request):
    return render(request, "main/seasonings_Russia.html")

def snacks_Russia(request):
    return render(request, "main/snacks_Russia.html")

def desserts_Russia(request):
    return render(request, "main/desserts_Russia.html")