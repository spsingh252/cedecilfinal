from django.db import models


# Create your models here.
class student (models.Model):
    student_name= models.CharField(max_length=50)
    email_id= models.CharField(max_length=50)
    age = models.IntegerField()
