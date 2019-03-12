from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(default='default.jpg',upload_to='project_pics')
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE)  
    goal = models.IntegerField(default=0) 
    current = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-details',kwargs={'pk': self.pk})
