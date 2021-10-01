from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #import user from tables
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # use user from table of users, if user is deleted, every blog of that author will be deleted
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()  # unrestricted text

    def __str__(self):
        return f"{str(self.title)},  '{str(self.author)}'"
