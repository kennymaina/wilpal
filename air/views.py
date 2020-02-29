from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django import template
from django.core.mail import send_mail
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from .forms import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            send_mail(
                'Sales Cargo',
                form_content,
                contact_email,
                ['kenmaina2022@gmail.com', 'info@wilpalinternationalogistics.com','imports@wilpalinternationalogistics.com','exports@wilpalinternationalogistics.com',
                 'wilber@wilpalinternationalogistics.com','paul@wilpalinternationalogistics.com','accounts@wilpalinternationalogistics.com','sales@wilpalinternationalogistics.com'],
                fail_silently=False,
            )
            messages.success(request,'The email has been sent successfully.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
             messages.warning(request, 'Something is not right. Please try again')
    return render(request, 'contact.html', locals())
