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

class department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

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
    dept = models.ForeignKey(department,on_delete=models.DO_NOTHING,null=True)
    post = models.CharField(max_length=30,null=True)
    cgpa_Req = models.DecimalField(max_digits=2,decimal_places=1,null=True)
    phd_Req = models.BooleanField(default=False,null=True)
    # spez_Req= models.ForeignKey(spez,on_delete=models.PROTECT)
    createdby = models.CharField(max_length=30,null=True)
    roundNum = models.PositiveSmallIntegerField(default=1)
    schedule = models.DateTimeField(null=True)
    
class application(models.Model):
    spez_Req= models.ForeignKey(spez,on_delete=models.PROTECT,null=True)
    job = models.ForeignKey(job,on_delete=models.PROTECT,null=True)
    dob = models.DateField()
    age = models.PositiveBigIntegerField()
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
    qualifications = models.CharField(max_length=30,choices=qual,null=True)
    cgpa = models.DecimalField(max_digits=2,decimal_places=1)
    experiance = models.PositiveBigIntegerField()
    citations = models.PositiveBigIntegerField()
    publications = models.PositiveBigIntegerField()
    country = models.CharField(max_length=40,null=True)
    city = models.CharField(max_length=40,null=True)
    state = models.CharField(max_length=40,null=True)
    district = models.CharField(max_length=40,null=True)
    postal = models.CharField(max_length=50,null=True)
    pincode = models.CharField(max_length=6,null=True)
    mob_num = models.CharField(max_length=10,null=True)
    hireScore = models.DecimalField(max_digits=3,decimal_places=2,null=True)
    user= models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    schedule = models.DateTimeField(null=True)
