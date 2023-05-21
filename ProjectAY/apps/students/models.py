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
    files = models.FileField(storage=RawMediaCloudinaryStorage(), null=True)
    notes = models.TextField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons", null=True)
    
    def get_file_url(self):
        if self.files:
            return self.files.storage.url(self.files.name)
        else:
            return None

class CourseTopic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.course.title
    