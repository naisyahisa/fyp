from django.db import models
from django.utils import timezone
#one user can author posts - one to many relationship, one post can have one author
from django.contrib.auth.models import User

#class = table, attribute = fields
class Post(models.Model):
    #field, with restriction
    title = models.CharField(max_length=100)
    #lines of text no restr.
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #passed in the user table, on-delete if the user got deleted, also posts got deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #to print out db, dunder method
    def __str__(self):
        return self.title 