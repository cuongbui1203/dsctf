from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, PermissionsMixin, AbstractUser


# Create your models here.

class Game(models.Model):
    gameID = models.AutoField(primary_key=True)
    gameIP = models.CharField(max_length=50)
    gamePort = models.CharField(max_length=50)
    gameName = models.CharField(max_length=50)
    gameRule = models.TextField(blank=True)
    gameSecretKey = models.CharField(max_length=50, blank=True)
    author = models.CharField(max_length=50, default='None')

    def __str__(self):
        return self.gameName


class Team(models.Model):
    teamID = models.AutoField(primary_key=True)
    teamSecretKey = models.CharField(max_length=50, unique=True)
    teamName = models.CharField(max_length=50, unique=True)
    teamScore = models.IntegerField(default=0)

    def __str__(self):
        return self.teamName


class User(AbstractUser, AbstractBaseUser):
    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    teamkey = models.CharField(max_length=50,default='')
    username = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=30)
    userScore = models.IntegerField(default=0)
    date_joined = models.DateTimeField(default=datetime.now())

    # def save(self, *args, **kwargs):
    #     user  = super(User, self)
    #     return  user

    def __str__(self):
        return self.email


class Alert(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
