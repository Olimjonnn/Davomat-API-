from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'teacher'),
        (2, 'pupil'),
    ), default=2)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Group(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name



class Pupil(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    parents_id = models.IntegerField(blank=True, null=True)

class Davomat(models.Model):
    day = models.CharField(max_length=30)
    time = models.CharField(max_length=200)
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    davomat = models.BooleanField(default=False)
