from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Company(models.Model):
  name = models.CharField(max_length=200, blank=True)
  description = models.TextField(blank=True, null=True)
  title = models.CharField(max_length=200, blank=True, null=True)
  package = models.CharField(max_length=200, blank=True, null=True)

  def __str__(self):
    return self.name

class Internship(models.Model):
  company = models.CharField(max_length=200)
  address = models.TextField(max_length=200)
  stipend = models.IntegerField(null=True, blank=True, default=0)
  role = models.CharField(max_length=200)

  def __str__(self):
    return self.company

class Student(models.Model):
  BRANCHES = (
    ('Civil Engineering', 'Civil Engineering'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'),
    ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'),
    ('Computer Science and Engineering', 'Computer Science and Engineering'),
    ('Electronics and Instrumentation Engineering', 'Electronics and Instrumentation Engineering'),
    ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'),
    ('Industrial Engineering and Management', 'Industrial Engineering and Management'),
    ('Information Science and Engineering', 'Information Science and Engineering'),
    ('Artificial Intelligence and Machine Learning', 'Artificial Intelligence and Machine Learning'),
  )

  user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
  phone = models.CharField(max_length=200, null=True, blank=True)
  first_name = models.CharField(max_length=200, null=True, blank=True)
  last_name = models.CharField(max_length=200, null=True, blank=True)
  usn = models.CharField(primary_key=True, max_length=200, null=False, blank=True)
  branch = models.CharField(max_length=100, null=True, choices=BRANCHES)
  company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
  resume = models.FileField(upload_to="resumes/",null=True, blank=True)
  
  profiles = ArrayField(models.URLField(max_length=1000, blank=True), default = list) #

  tenthgrade = models.CharField(max_length=20,blank=True, null=True)
  twelvegrade = models.CharField(max_length=20,blank=True, null=True)
  Diploma = models.CharField(max_length=20,blank=True, null=True)
  ug = models.CharField(max_length=20,blank=True, null=True)
  pg = models.CharField(max_length=20,blank=True, null=True)
  extracurricular = models.TextField(blank=True, null=True)
  clubs = models.TextField(blank=True, null=True)
  certificates = ArrayField(models.URLField(max_length=1000), size = 20, null=True, blank=True, default = list) #
  projects = models.TextField(blank=True, null =True)
  projectslinks = ArrayField(models.URLField(max_length=1000), size = 20, null=True, blank=True, default = list) #
  internships = models.ForeignKey(Internship, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    return self.usn

class Resource(models.Model):
  aptitute = models.FileField(upload_to="amplitude/", null=True, blank=True)
  technical = models.FileField(upload_to="technical/", null=True, blank=True)
  vandc = models.FileField(upload_to="vandc/", null=True, blank=True)
  logicalresoning = models.FileField(upload_to="logicalresoning/", null=True, blank=True)
  def __str__(self):
    return self.id




