
from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    username = models.ForeignKey(User, null='False')
   
    def __unicode__(self):
        return self.username

class UserAddress(models.Model):
    username = models.ForeignKey(User, null='False')
    streetNumber = models.CharField(max_length=10 null='False')
    streetName = models.CharField(max_length=50, null='False')
    unit = models.CharFields(max_length=10, null='True')
    city = models.CharField(max_length=100, null='False')
    state = models.CharField(max_length=3, null='False')
    zipCode = models.CharField(max_length=15, null='False')
    country = models.CharField(max_length=20, null='True')
    isDefault = models.BooleanField()

    def __unicode__(self):
        return self.streetNumber, ' ',  self.streetName, ' ', 
        self.unit, '\n', self.city, ', ', self.state, ' ', self.zipCode


   
