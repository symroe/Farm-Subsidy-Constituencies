from django.db import models

# "globalRecipientId","name","address","zipcodeUK","town","countryRecipient","constituency","amount"


class Constituency(models.Model):
    name = models.CharField(blank=True, max_length=100)
    slug = models.SlugField()
    total = models.FloatField(null=True)
    recipients = models.IntegerField(blank=True, null=True)
    average = models.FloatField(null=True)
    
    def __unicode__(self):
        return u"%s" % self.name

class Recipient(models.Model):
    globalrecipientid = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True, max_length=255)
    postcode = models.CharField(blank=True, max_length=12)
    town = models.CharField(blank=True, max_length=255)
    country = models.CharField(blank=True, max_length=4)
    amount = models.FloatField()
    constituency = models.ForeignKey(Constituency)
    
    def __unicode__(self):
        return u"%s" % self.name
    