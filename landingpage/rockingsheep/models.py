from django.db import models

class Email(models.Model):
    ip_address = models.IPAddressField()
    send_date = models.DateTimeField()
    send_address = models.EmailField()
    error_css_class = 'error'
    required_css_class = 'required'