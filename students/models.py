from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.
class Student(models.Model) :
    first_name = models.CharField(max_length=50 , null= False, blank= False )
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MaxValueValidator(120) , MinValueValidator(0)])
    birth_date = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=1)
    
    def __str__(self)  : 
        return self.first_name + " " + self.last_name
