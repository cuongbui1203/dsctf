from django.db import models
from datetime import datetime


# Create your models here.

class Game(models.Model):
    gameID = models.PositiveIntegerField(primary_key=True)
    gameIP = models.CharField(max_length=50, unique=True)
    gamePort = models.CharField(max_length=50, unique=True)
    gameName = models.CharField(max_length=50, unique=True)
    gameRule = models.TextField(blank=True)
    gameSecretKey = models.CharField(max_length=50, blank=True)


class Team(models.Model):
    teamID = models.PositiveIntegerField(primary_key=True)
    teamSecretKey = models.CharField(max_length=50, unique=True)
    teamName = models.CharField(max_length=50, unique=True)
    teamScore = models.IntegerField(default=0)


class User(models.Model):
    userID = models.PositiveIntegerField(primary_key=True)
    role = models.IntegerField(default=0)
    teamID = models.ForeignKey(Team, on_delete=models.CASCADE)
    userName = models.CharField(max_length=50, unique=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=30)
    userScore = models.IntegerField(default=0)
    timeCreate = models.DateTimeField(default=datetime.now(), blank=True)
    timeChange = models.DateTimeField(blank=True)

class Alert(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now())

