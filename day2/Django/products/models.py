from django.db import models
# Create your models here.
class Author(models.Model): #작가
    name = models.CharField(max_length=60) #이름
    location = models.CharField(max_length=60) #위치
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Book(models.Model): #Book Prouduct
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name="books")
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=120)
    price = models.PositiveBigIntegerField()
    shipping_cost = models.IntegerField()
    quantity = models.PositiveBigIntegerField()
    

    def __str__(self):
        return  f"{self.name} by {self.author.name}"




