from django.db import models

# Create your models here.
class allcourses(models.model):
    coursename=models.CharField(max_length=200)
    insname=models.CharField(max_length=100)

class details(models.model):
    course = models.ForeignKey(allcourses,on_delete=models.CASCADE)
    sp = models.CharField(max_length=300)
    lp = models.CharField(max_length=300)


