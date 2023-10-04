from django.db import models

class student(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    dob = models.DateField()  
    qualification = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    image= models.ImageField(blank=True,upload_to="image/",default='static/images/default.jpg', null=True)

# Create your models here.
