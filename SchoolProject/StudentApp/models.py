from django.db import models
from django.db.models import Model
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=90)
    course = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    rollno = models.IntegerField(default=0)
    fees = models.FloatField(default=0)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5}".format(self.name, self.course, self.gender, self.rollno, 
        self.fees, self.pub_date)
