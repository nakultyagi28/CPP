from django.db import models
from django.contrib.auth.models import AbstractUser


def tutorial_video_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/2015/tutorial_<id>/<filename>
    return '%Y/tutorial_{0}/{1}'.format(instance.tutorial.id, filename)


class Course(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
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


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Admin ID: {self.user.id} & Name: {self.user.username}"


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Professor ID: {self.id} & Name: {self.username}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Student ID: {self.user.id} & Name: {self.user.username}"

class Tutorial(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    module = models.ForeignKey(Module, on_delete=models.DO_NOTHING)
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
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    video = models.FileField(upload_to=tutorial_video_directory_path,blank=True,null=True)

    def __str__(self):
        return f"Video ID: {self.id} & Name: {self.title}"

    def delete(self, *args, **kwargs):
        self.video.delete()
        super().delete(*args, **kwargs) 

