from turtle import title
from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.text


class ILoveModels(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    stock = models.IntegerField()
    def __str__(self):
        return self.title

class BoughtModel(models.Model):
    title = models.CharField(max_length=200)
    quantity = models.IntegerField()
    def __str__(self):
        return self.title
