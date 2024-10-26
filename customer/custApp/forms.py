from django import forms
from .models import *
class userform(forms.ModelForm):
    class Meta:
        model=user
        fields= "__all__"


def clean_name(self):
    name=self.cleaned_data.get('name')
    if " " in name:
        raise forms.ValidationError(" avoid whitspace in the name")
    return name
      
def claen_email(self):
    email= self.cleaned_data.get('email')
    if user.objects.filter(email=email).exists():
        raise forms.validationError("email is already in use")
    return email