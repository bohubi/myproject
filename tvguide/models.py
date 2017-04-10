from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=40)


class Category(models.Model):
    name = models.CharField(max_length=40)


class Program(models.Model):
    name = models.CharField(max_length=200)
    duration_in_minutes = models.IntegerField()
    release_year = models.IntegerField()
    category = models.ForeignKey(Category)


class TimeSlot(models.Model):
    start = models.DateTimeField()
    finish = models.DateTimeField()
    channel = models.ForeignKey(Channel)
    program = models.ForeignKey(Program)


class Genre(models.Model):
    name = models.CharField(max_length=40)


class ProgramGenre(models.Model):
    program = models.ForeignKey(Program)
    genre = models.ForeignKey(Genre)















# from django.db import models
#
#
# # Create your models here.
# class Channel(models.Model):
#     name = models.CharField(max_length=50)
#
#
#     def __str__(self):
#         return self.name
#
# class Category(models.Model):
#     name = models.CharField(max_length=200)
#
# class Program(models.Model):
#     name = models.CharField(max_length=200)
#     duration_in_minutes = models.IntegerField()
#     release_year = models.IntegerField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
# class TimeSlot(models.Model):
#     start = models.DateTimeField('date published')
#     finish = models.DateTimeField('date published')
#     channel = models.ForeignKey(Channel)
#     program = models.ForeignKey(Program)
#
# class Genre(models.Model):
#     name = models.CharField(max_length=200)
#
# class ProgramGenre(models.Model):
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


