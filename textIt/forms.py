from django.forms import ModelForm, TextInput, Textarea, URLInput, EmailInput, forms
from .models import Recipient, Contact
from django.utils.translation import ugettext_lazy as _


class RecipientForm(ModelForm):

    class Meta:
        model = Recipient
        fields = ['provider','receiving_number','url_link']
        widgets = {
            'receiving_number': TextInput(attrs={'placeholder': '555-555-5555'}),
            'url_link': URLInput(attrs={'placeholder': 'www.mylink.com'}),
        }



class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'John Smith'}),
            'email': EmailInput(attrs={'placeholder': 'email@provider.com'}),
            'message': Textarea(attrs={'placeholder': 'Enter text here'}),
        }

