from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class SuperPlayer(models.Model):
    # name = models.IntegerField(default=50,min_value=0, max_value=100)
    name=models.CharField(max_length=300)
    score = models.IntegerField(
        default=50,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
     )
    country = models.CharField(max_length=100)
    addBy = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


    
    #  default=1,validators=[MaxValueValidator(100),MinValueValidator(1)]