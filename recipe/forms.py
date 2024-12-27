from .models import Articles
from django.forms import ImageField, ModelForm, TextInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['country', 'title', 'descriptions', 'cooking', 'products', 'dish', 'tableware', 'time']

        widgets = {
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Национальная кухня'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название блюда'
            }),
            'descriptions': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'cooking': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Как приготовить'
            }),
            'products': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ингредиенты'
            }),
            'dish': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип блюда ( Первое, второе, маринад, приправа, закуска, десерт )'
            }),
            'tableware': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'в какой посуде готовилось'
            }),
            'time': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время приготовления ( в минутах )'
            }),
        }