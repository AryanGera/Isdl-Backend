from email.policy import default
from enum import unique
from logging import debug
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class post(models.Model):
    name = models.CharField(max_length=100)
    
class department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

class spez(models.Model):
    name = models.CharField(max_length=100)
    dept=models.ForeignKey(department,on_delete=models.CASCADE)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    cse_Acess = models.BooleanField(default=False)
    mec_Acess = models.BooleanField(default=False)
    cce_Acess = models.BooleanField(default=False)
    ece_Acess = models.BooleanField(default=False)
    username=None
    USERNAME_FIELD ="email"
    REQUIRED_FIELDS = []
class job(models.Model):
    dept = models.ForeignKey(department,on_delete=models.CASCADE)
    post = models.CharField(max_length=30)
    cgpa_Req = models.DecimalField(max_digits=2,decimal_places=1,default=0)
    phd_Req = models.BooleanField(default=False)
    spez_Req= models.ForeignKey(spez,on_delete=models.DO_NOTHING)
    createdby = models.CharField(max_length=30)
    
    

class application(models.Model):
    spez= models.ForeignKey(spez,on_delete=models.DO_NOTHING)
    
    job = models.ForeignKey(job,on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    age = models.PositiveBigIntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    Title_ch = (
        ('1','Mrs.'),
        ('2','Mr.'),
        ('3','Dr.'),
        ('4','Ms.'),
    )
    title = models.CharField(max_length=5,choices=Title_ch)
    father = models.CharField(max_length=40,null=True)
    mother = models.CharField(max_length=40,null=True)
    CAT_CHOICES = (
        ('1','GEN'),
        ('2','SC'),
        ('3','ST'),
        ('4','OBC'),
    )
    category = models.CharField(max_length=5,choices=CAT_CHOICES)
    Nationality = models.CharField(max_length=30)
    
    qual = (
        ('1','B.A.'),
        ('2','B.Arch.'),
        ('3','BSc'),
        ('4','MSc'),
        ('5','B.Tech'),
        ('6','M.Tech'),
        ('7','PhD'),
    )
    qualifications = models.CharField(max_length=30,choices=qual)
    cgpa = models.DecimalField(max_digits=4,decimal_places=2)
    experiance = models.PositiveBigIntegerField(default=0)
    citations = models.PositiveBigIntegerField(default=0)
    publications = models.PositiveBigIntegerField(default=0)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    postal = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    mob_num = models.CharField(max_length=10)
    hireScore = models.DecimalField(max_digits=3,decimal_places=2,null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    schedule = models.DateTimeField(null=True)
    roundNum = models.PositiveSmallIntegerField(default=1)

