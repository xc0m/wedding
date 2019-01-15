from django import forms

from .models import Rsvp


class EventRSVPForm(forms.ModelForm):
    class Meta:
        model = Rsvp
        fields = ['guestOne', 'guestTwo', 'phonenumber', 'address', 'status', 'comment']
        widgets = {
            'status': forms.RadioSelect(
                 attrs={
                    'display': 'inline-block',
                 }
            ),

        }
