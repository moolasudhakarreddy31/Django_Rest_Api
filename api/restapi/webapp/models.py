from django.db import models

# Create your models here.

class Employee(models.Model):
    empid=models.IntegerField()
    empfirstname=models.CharField(max_length=30)
    emplastname=models.CharField(max_length=30)


    def __str__(self):
        return self.empfirstname
