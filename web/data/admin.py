from django.contrib import admin
from data.models import Constituency, Recipient

class ConstituencyAdmin(admin.ModelAdmin):
  list_display  = ('name','total', 'recipients','average',)


admin.site.register(Constituency, ConstituencyAdmin)
admin.site.register(Recipient)
