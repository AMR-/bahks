
from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    username = models.ForeignKey(User, null=False)
    #userType = models.CharField(max_length=30,null=False)
   
    def __unicode__(self):
        return self.username

class Address(models.Model):
    username = models.ForeignKey(User, null=False)
    streetNumber = models.CharField(max_length=10 null=False)
    streetName = models.CharField(max_length=50, null=False)
    unit = models.CharFields(max_length=10, null=True)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=3, null=False)
    zipCode = models.CharField(max_length=15, null=False)
    country = models.CharField(max_length=20, null=True)
    isDefault = models.BooleanField()

    def __unicode__(self):
        return self.streetNumber, ' ',  self.streetName, ' ', 
        self.unit, '\n', self.city, ', ', self.state, ' ', self.zipCode

class Box(models.Model):
    orderID = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, null=False)
    # how do we associate with a warehouse time?
    length = models.DecimalField(max_digits= 6, decimal_places=2, null=True)
    width = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    orderDate = models.DateTimeField(auto_now_add=True)
    storageStartDate = models.DateTimeField(null=True)
    cubFeet = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    tier1 = 'Tier 1'
    tier2 = 'Tier 2'
    tier = models.CharField(max_length=7, null=True,
                            choices = ((tier1, 'Tier 1'), 
                                (tier2, 'Tier 2')) )
    labled = 'Labled'
    received = 'Received'
    retrieved = 'Retrieved'
    status = model.CharField(max_length=10, null=True, 
                            choices = ((labled, 'Labled'),
                                (received, 'Received'),
                                (retrieved, 'Retrieved'))

    def calculateFee(self):
        """
        $1.85 for retrieval
        $4 per month for unlimited boxes
        collected semi-annually

        2nd tier (boxes not broken down):
        $1 per month per sq foot
        $1.85 for 2lbs + .50 cents per lb

        """

    def __unicodes__(self):
        return 'orderID: ',orderID,'\n','username: ',username,'\n','order date: ',
        orderDate,'\n','storage start date: ',storageStartDate,'\n','cubic feet: ',
            cubFeet, 'weight: ', weight, 'tier: ', tier
