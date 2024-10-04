from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    view_num = models.IntegerField(default=0)
    pub_time = models.DateTimeField()
    userID = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    def save_post(self, password):
        self.pub_time = timezone.now()
        self.password = password
        self.save()

    def view_num_up(self):
        self.view_num = self.view_num + 1
        self.save()