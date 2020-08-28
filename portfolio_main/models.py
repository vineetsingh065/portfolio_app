from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Main(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    about = models.TextField()
    contact = models.CharField(default='0', max_length=12)
    email = models.CharField(default='-', max_length=50)
    linkedin = models.CharField(default='-', max_length=50)
    github = models.CharField(default='-', max_length=50)
    twitter = models.CharField(default='-', max_length=50)
    facebook = models.CharField(default='-', max_length=50)
    site_name = models.CharField(default='-', max_length=50)
    resume = models.FileField()
    cover_letter = models.FileField()
    user_pic = models.ImageField()


    def __str__(self):
        return self.site_name + "|" + str(self.pk)


class TechnicalSkills(models.Model):

    skill_name = models.CharField(max_length=50)
    confidence = models.CharField(max_length=50)


class Experience(models.Model):

    role = models.CharField(max_length=50)
    organisation = models.CharField(max_length=50)
    role_description = models.CharField(max_length=50)
    start_from = models.CharField(max_length=50)
    till = models.CharField(max_length=50)


class Accomplishment(models.Model):

    accolade = models.CharField(max_length=50)


class Projects(models.Model):

    project = models.CharField(max_length=50)
    organisation = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    start_from = models.CharField(max_length=50)
    till = models.CharField(max_length=50)


class Education(models.Model):

    institute = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    score = models.CharField(max_length=50)
    start_from = models.CharField(max_length=50)
    till = models.CharField(max_length=50)



