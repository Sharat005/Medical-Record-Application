from django.db import models

# Create your models here.

class User(models.Model):

  first_name = models.CharField(max_length=50, default='Anonymous')
  middle_name = models.CharField(max_length=50, blank=True, null=True)
  last_name = models.CharField(max_length=50, default='Anonymous')

  email = models.EmailField(max_length=254, unique=True)
  phone = models.CharField(max_length=20, blank=True, null=True)
  gender = models.CharField(max_length=10, blank=True, null=True)
  dob = models.DateField(max_length=10, blank=True, null=True)
  age = models.CharField(max_length=20, blank=True, null=True)
  race = models.CharField(max_length=20, blank=True, null=True)
  ethnicity = models.CharField(max_length=20, blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  address = models.CharField(max_length=500, blank=True, null=True, default='Anonymous')
  city = models.CharField(max_length=50, blank=True, null=True, default='Anonymous')
  state = models.CharField(max_length=50, blank=True, null=True, default='Anonymous')
  zipcode = models.CharField(max_length=6)

  def __str__(self):
    return self.first_name
