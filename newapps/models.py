from django.db import models
from django.contrib.auth.forms import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Software Engineer', 'software engineer')
        ('Test Engineer', 'test engineer')
        ('Dev Ops', 'dev ops')
        ('Scrum Master', 'scrum master')
        ('Product Owner', 'product owner')
    
    
    )    
    role = models.CharField(choices=ROLE_CHOICES, default='user')

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=255)

    role = models.CharField(max_length=100)

    idea_ID = models.CharField(max_length=20)

    idea_name = models.CharField(max_length=100)

    idea_description = models.CharField(max_length=255)

    idea_dependencies = models.CharField(max_length=255)

    idea_comments = models.CharField(max_length=300)

    idea_votes = models.CharField(max_length=100)


    def __str__(self):

        return self.first_name + "   " + self.last_name
    

