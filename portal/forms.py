from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)


FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),('green', 'Green'),('black', 'Black'))


class Registration_Form(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    favorite_colors = forms.MultipleChoiceField(required=False,widget=CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)

