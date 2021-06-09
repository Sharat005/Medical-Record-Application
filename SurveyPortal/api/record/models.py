from distutils.log import info
from tkinter.tix import Tree
from django.db import models
from api.user.models import User

# Create your models here.

class Record(models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


  copd = models.BooleanField(default=False, blank=True)
  copd_flare = models.BooleanField(default=False, blank=True)
  smoked = models.BooleanField(default=False, blank=True)
  smoke_count = models.IntegerField(default=0, blank=True, null=True)
  yearsSmoked = models.IntegerField(default=0, blank=True)
  packyears = models.IntegerField(default=0, blank=True)
  smoking_start_age = models.IntegerField(default=0, blank=True, null=True)
  smoking_stop_age = models.IntegerField(default=0, blank=True, null=True)

  pregnant = models.BooleanField(default=False, blank=True)
  asthma = models.BooleanField(default=False, blank=True)
  ashthma_age = models.IntegerField(default=0, blank=True, null=True)
  lung_disease = models.BooleanField(default=False, blank=True)
  lung_disease_desc = models.CharField(max_length=50, blank=True, null=True)
  antibiotics = models.BooleanField(default=False, blank=True)
  bp_medicine = models.BooleanField(default=False, blank=True)
  bp_medicine_list = models.CharField(max_length=50, blank=True, null=True)

  glaucome = models.BooleanField(default=False, blank=True)
  diabetes = models.BooleanField(default=False, blank=True)
  lung_cancer = models.BooleanField(default=False, blank=True)
  clinical_trial = models.BooleanField(default=False, blank=True)
  atrial = models.BooleanField(default=False, blank=True)
  atrial_therapy = models.BooleanField(default=False, blank=True)
  atrial_controlled = models.BooleanField(default=True, blank=True)
  bph = models.BooleanField(default=False, blank=True)
  bph_stable = models.BooleanField(default=True, blank=True)

  info = models.CharField(max_length=50, blank=True, null=True)
  info_other = models.CharField(max_length=500, blank=True, null=True)
  other_comments = models.CharField(max_length=500, blank=True, null=True)
