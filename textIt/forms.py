from django.forms import ModelForm, TextInput, Textarea, URLInput, EmailInput, forms
from .models import Recipient, Contact, UserContact
from django.utils.translation import ugettext_lazy as _

#Form to send texts for unregistered users
#
class RecipientForm(ModelForm):

    class Meta:
        model = Recipient
        fields = ['provider','receiving_number','url_link', 'message']
        widgets = {
            'receiving_number': TextInput(attrs={'placeholder': '555-555-5555'}),
            'url_link': URLInput(attrs={'placeholder': 'http://www.mylink.com'}),
            'message': Textarea(attrs={'placeholder': 'Optional Message Here'}),
        }


#Form to send texts for registered users
#
class RegRecipientForm(ModelForm):

    class Meta:
        model = Recipient
        fields = ['receiving_name','url_link', 'message']
        widgets = {
            'receiving_name': TextInput(attrs={'placeholder': 'Enter Contact Name'}),
            'url_link': URLInput(attrs={'placeholder': 'http://www.mylink.com'}),
            'message': Textarea(attrs={'placeholder': 'Optional Message Here'}),
        }


#Form that allows users to add contacts
#
class AddContactForm(ModelForm):

    class Meta:
        model = UserContact
        fields = {'contact_provider', 'contact_name', 'phone_number'}
        widgets = {
            'contact_name': TextInput(attrs={'placeholder': 'Enter Contact Name'}),
            'phone_number': URLInput(attrs={'placeholder': '555-555-5555'}),
        }


#Main contact form for the site
#
class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'contact_message']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Your Name'}),
            'email': EmailInput(attrs={'placeholder': 'email@provider.com'}),
            'contact_message': Textarea(attrs={'placeholder': 'Enter text here'}),
        }

