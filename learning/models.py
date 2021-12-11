from django.db import models
from django.contrib.auth.models import AbstractUser


def tutorial_video_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/2015/tutorial_<id>/<filename>
    return '%Y/tutorial_{0}/{1}'.format(instance.tutorial.id, filename)


class Course(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"Course ID: {self.id} & Name: {self.id}"


class Module(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"Module ID: {self.id} & Name: {self.name}"


class Admin(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"Admin ID: {self.id} & Name: {self.username}"


class Professor(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"Professor ID: {self.id} & Name: {self.username}"


class Student(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    course = models.ForeignKey(Course)

    def __str__(self):
        return f"Student ID: {self.id} & Name: {self.username}"

class Tutorial(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    module = models.ForeignKey(Module)
    professors = models.ManyToManyField(Professor)
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f"Tutorial ID: {self.id} & Name: {self.title}"

    def delete(self, *args, **kwargs):
        self.thumbnail.delete()
        super().delete(*args, **kwargs)  


class TutorialVideo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    tutorial = models.ForeignKey(Tutorial)
    video = models.FileField(upload_to=tutorial_video_directory_path,blank=True,null=True)

    def __str__(self):
        return f"Video ID: {self.id} & Name: {self.title}"

    def delete(self, *args, **kwargs):
        self.video.delete()
        super().delete(*args, **kwargs) 

