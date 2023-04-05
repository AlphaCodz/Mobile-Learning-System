from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    files = models.FileField(storage=RawMediaCloudinaryStorage(), null=True)
    notes = models.TextField(null=True)
    
    def get_file_url(self):
        if self.files:
            return self.files.storage.url(self.files.name)
        else:
            return None
    
class Course(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=10)
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, null=True)
    
    
    def __str__(self):
        return self.title
    

class CourseTopic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.course.title
    