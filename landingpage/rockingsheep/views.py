#from django.http import HttpResponse
#from django.shortcuts import render_to_response

#from django.views.generic.simple import direct_to_template
from django import forms
import logging

logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    send_address = forms.EmailField()

from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return email_and_thanks(request, form)
    else:
        form = ContactForm()
    return render(request, 'rockingsheep/contact.html', {
                                            'form' : form
                                            })
    
#    return render_to_response('rockingsheep/index.html')
#    return direct_to_template(request,'rockingsheep/contact.html')



def email_and_thanks(request, form):
    from django.utils import timezone
    send_date = timezone.now()
    ip_address = get_client_ip(request)
    subject = "Kontakt fra Rokkefaar"
    
    sender = form.cleaned_data['send_address']
    message = "Person med email:" + sender + " og IP: " + ip_address
    recipients = ['emil@kjer.info']

    
    from rockingsheep.models import Email
    e = Email(send_date=send_date, send_address=sender, ip_address=ip_address)
    
    e.save()
    
    # Send email
    # https://docs.djangoproject.com/en/dev/topics/email/
    from django.core.mail import send_mail
    result = send_mail(subject, message, sender, recipients)
    logger.info('Email send. SUBJECT:%s, MESSAGE:%s, SENDER:%s' %(subject, message, sender))
    return render(request, 'rockingsheep/thanks.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
