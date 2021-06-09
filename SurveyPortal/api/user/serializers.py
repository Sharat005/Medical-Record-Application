from curses.ascii import US
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name',
        'middle_name',
        'last_name',
        'dob',
        'gender',
        'email',
        'phone',
        'race',
        'ethnicity',
        'address',
        'city',
        'state',
        'zipcode')