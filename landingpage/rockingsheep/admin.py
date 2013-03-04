from rockingsheep.models import Email
from django.contrib import admin

class EmailAdmin(admin.ModelAdmin):
    list_display = ('send_address', 'send_date')
#    list_filter = ['send_date']
#    search_fields = ['send_address']
admin.site.register(Email)

