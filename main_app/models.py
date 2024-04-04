from django.db import models
from datetime import date
# Create your models here.

class Happymeal(models.Model):
    date = models.DateField('Date the toy was made')
    price = models.IntegerField()

def __str__(self):
    return self.name

class Burger(models.Model):
    name = models.CharField(max_length = 100)
    burgertype = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
    age = models.IntegerField()
    happymeal= models.ManyToManyField(Happymeal)
def __str__(self):
    return self.name


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
) 
def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)



class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField( max_length=1, choices=MEALS,default=MEALS[0][0])
    burger= models.ForeignKey(Burger, on_delete=models.CASCADE)
  
def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

class Meta:
    ordering = ['-date']

