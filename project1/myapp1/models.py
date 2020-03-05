from django.db import models

# Create your models here.
class Employee(models.Model):

	name = models.CharField(max_length=50)
	email = models.EmailField()
	mobile = models.BigIntegerField()
	salary = models.IntegerField()

	class Meta:
		db_table = 'employee'