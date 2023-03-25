from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=10)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Topic(models.Model):
    name = models.CharField(max_length=200)
    note_file = models.FileField(storage=RawMediaCloudinaryStorage())
    notes = models.TextField()
    
    def get_file_url(self):
        return self.note_file.storage.url(self.note_file.name)
    
    