from __future__ import unicode_literals

from django.db import models

# Create your models here.

Providers = {
    ('@txt.att.net', 'AT&T'),
    ('@mms.cricketwireless.net', 'Cricket'),
    ('@tmomail.net', 'T-Mobile'),
    ('@pm.sprint.com', 'Sprint'),
    ('@vtext.com', 'Verizon')

}


class Recipient(models.Model):
    recipient = models.CharField(max_length=200, default="NULL")
    sender = models.CharField(max_length=200, default="NULL")
    receiving_number = models.CharField(max_length=20)
    receiving_name = models.CharField(max_length=200)
    message = models.TextField(max_length=500, null=True, blank=True)
    url_link = models.URLField(max_length=1000, null=True, blank=True)
    provider = models.CharField(max_length=20, choices=Providers, null=True)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact_message = models.TextField(max_length=1000)


class UserContact(models.Model):
    linkedUser= models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    contact_name =models.CharField(max_length=200)
    contact_provider = models.CharField(max_length=20, choices=Providers)



