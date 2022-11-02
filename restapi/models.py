from email.policy import default
from enum import unique
from logging import debug
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class spez(models.Model):
    name = models.CharField(max_length=50)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    USERNAME_FIELD ="email"
    REQUIRED_FIELDS = []
class job_App(models.Model):
    dept_name = models.CharField(max_length=45)
    post = models.CharField(max_length=30)
    cgpa_Req = models.DecimalField(max_digits=2,decimal_places=1)
    phd_Req = models.BooleanField(default=False)
    spez_Req= models.ForeignKey(spez,on_delete=models.PROTECT)
    cse_Acess = models.BooleanField(default=False)
    mec_Acess = models.BooleanField(default=False)
    cce_Acess = models.BooleanField(default=False)
    ece_Acess = models.BooleanField(default=False)
    hum_Acess = models.BooleanField(default=False)
class application(models.Model):
    user = models.OneToOneField('User',related_name='applicant',on_delete=models.CASCADE)
    spez_Req= models.ForeignKey(spez,on_delete=models.PROTECT)
    application = models.ForeignKey(job_App,on_delete=models.PROTECT)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Rather Not Say')
    )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    Title_ch = (
        ('1','Mrs.'),
        ('2','Mr.'),
        ('3','Dr.'),
        ('4','Ms.'),
    )
    title = models.CharField(max_length=5,choices=Title_ch,null=True)
    father = models.CharField(max_length=40,null=True)
    mother = models.CharField(max_length=40,null=True)
    CAT_CHOICES = (
        ('1','GEN'),
        ('2','SC'),
        ('3','ST'),
        ('4','OBC'),
    )
    category = models.CharField(max_length=5,choices=CAT_CHOICES,null=True)
    Nationality = models.CharField(max_length=30,null=True)
    
    qual = (
        ('1','B.A.'),
        ('2','B.Arch.'),
        ('3','BSc'),
        ('4','MSc'),
        ('5','B.Tech'),
        ('6','M.Tech'),
        ('7','PhD'),
    )
    Nationality = models.CharField(max_length=30,choices=qual,null=True)




class admin(models.Model):
    user = models.OneToOneField('User',related_name='admin',on_delete=models.CASCADE)
    
    

    