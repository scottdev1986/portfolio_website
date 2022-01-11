from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.checks import messages
from django.contrib import messages
from .forms import ContactForm
from decouple import config

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [config('EMAIL_HOST_USER')], fail_silently=False)
                messages.success(request, 'Your email has been sent')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/#contact')
        else:
            messages.error(request, 'Please verify CAPTCHA')
    
    return redirect('/#contact')
