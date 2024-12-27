from django.db import models

class Articles(models.Model):
    country = models.CharField ('Национальная кухня', max_length=50)
    title = models.CharField('Название блюда', max_length=100)
    photo = models.ImageField(upload_to='media')
    descriptions = models.CharField('Описание', max_length=150)
    cooking = models.TextField('Как приготовить')
    products = models.TextField('Ингредиенты')
    dish = models.CharField('Тип блюда', max_length=50)
    tableware = models.TextField('Тип приготовления')
    time = models.CharField('Время приготовления', max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name ='Рецепт'
        verbose_name_plural = 'рецепты'