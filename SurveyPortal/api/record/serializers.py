from curses.ascii import US
from rest_framework import serializers

from .models import Record

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('id', 'user', 'smoked',
      'copd',
      'copd_flare',
      'bp_medicine',
      'pregnant',
      'asthma',
      'lung_disease',
      'lung_cancer',
      'glaucome',
      'clinical_trial',
      'atrial',
      'atrial_therapy',
      'atrial_controlled',
      'bph',
      'bph_stable',
      'smoking_start_age',
      'smoking_stop_age',
      'bp_medicine_list',
      'smoke_count',
      'ashthma_age',
      'lung_disease_desc',
      'info',
      'info_other',
      'other_comments')