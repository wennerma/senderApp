from django.shortcuts import render
from .forms import RecipientForm, ContactForm
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import Contact, Recipient

from .models import Recipient


# Home Page
# If loading the page without form submission, initialize the forms
#
def index(request):

    if request.method == "GET":
        form = RecipientForm()
        contact = ContactForm()

    return render(request, 'textIt/index.html', {
        "form": form,
        "contact": contact
    })

# Function to send text messages
# This function should only be called during form submission via ajax call
# Utilizes Djano send_mail('Subject', "Body", "Email Server", "Receiving Email Address", "ERRORS")
# The Receiving email address is a 10 digit phone number provided + extension based on carrier
# Carrier extension defined in the model
# Utilizes Gmail mail servers
#
def send_text(request):

    if request.method == "GET":
        return HttpResponse("ERROR")

    else:
        provider = request.POST.get('provider', '')
        url_link = request.POST.get('url_link', '')
        receiving_number = request.POST.get('receiving_number', '')
        optMessage = request.POST.get('message', '')

        #generate random code to send in subject, and display back to browser
        msgCode = random.randint(1,10000)

        bodyToSend = optMessage + "\n" + url_link
        plainNumber = receiving_number.replace("-", "")

        sendToNumber = plainNumber + provider

        send_mail(msgCode, bodyToSend,  settings.EMAIL_HOST_USER,
                 [sendToNumber], fail_silently=False)

        #save log of text sent to database
        recipient = Recipient(provider=provider, url_link=url_link, receiving_number=receiving_number)
        recipient.save()

        data = {'provider': provider, 'url_link': url_link, 'receiving_number': receiving_number,
                'sendToNumber': sendToNumber, 'msgCode': msgCode}


        return JsonResponse(data)


# Function to contact admin
# This function should only be called during form submission via ajax call
# Utilizes Djano send_mail('Subject', "Body", "Email Server", "Receiving Email Address")
# Utilizes Gmail mail servers
#
def contact(request):

    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')

        email_message = name + " \n" + message + "\n" + email
        contactEmail = 'wennerma@gmail.com'

        send_mail('Contact', email_message,  settings.EMAIL_HOST_USER,
                [contactEmail], fail_silently=False)

        data = {'name': name}

        return JsonResponse(data)






