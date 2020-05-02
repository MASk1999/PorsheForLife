from django.db import models

# Create your models here.
class cars(models.Model):
    chass_num = models.CharField(max_length=20, primary_key=True)
    car_model = models.CharField(max_length=10)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.chass_num

class owners(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    phone = models.IntegerField(unique=True)
    address = models.TextField()
    email = models.EmailField()
    car_owned = models.ForeignKey('cars', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
