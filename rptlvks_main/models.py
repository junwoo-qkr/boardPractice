from django.db import models

# Create your models here.
class rptlrmf(models.Model):
    title = models.CharField(max_length=50)
    publisher = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    text = models.TextField()
    view_num = models.IntegerField()