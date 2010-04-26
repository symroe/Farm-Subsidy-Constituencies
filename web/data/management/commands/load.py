import django
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand, CommandError
import csv
from data.models import Constituency, Recipient
from django.db.models import Sum, Max, Count

# "globalRecipientId","name","address","zipcodeUK","town","countryRecipient","constituency","amount"

class Command(BaseCommand):
    def populate(self):
        f = open("../constituency.csv")
        f = csv.DictReader(f)

        for line in f:
            
            try:
                c = Constituency.objects.get(name=line['constituency'])
            except Exception, e:
                c = Constituency(name=line['constituency'], slug=slugify(line['constituency']))
                c.save()
            
            try:
                # If this object exists, then no need to do anything more
                Recipient.objects.get(globalrecipientid=line['globalRecipientId'])
            except Exception, e:
                r = Recipient(
                    globalrecipientid = line['globalRecipientId'],
                    name = line['name'],
                    address = line['address'],
                    postcode = line['zipcodeUK'],
                    town = line['town'],
                    country = line['countryRecipient'],
                    amount = line['amount'],
                    constituency = c,
                )
                r.save()
    
    def totals(self):
        totals = Recipient.objects.values('constituency').annotate(
            count=Count('pk'),
            total=Sum('amount'),
        ).order_by('constituency')
        
        
        for total in totals:
            c = Constituency.objects.get(pk=total['constituency'])
            c.total = total['total']
            c.recipients = total['count']
            c.average = c.total/c.recipients
            c.save()
        
    def handle(self, **options):
        self.populate()
        self.totals()




