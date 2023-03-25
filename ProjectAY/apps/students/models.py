from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=10)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    