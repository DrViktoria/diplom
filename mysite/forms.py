from django import forms
from .models import *


class SubscribersForms(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = [""]