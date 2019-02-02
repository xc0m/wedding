from django import forms

from .models import Rsvp

class RSVPForm(forms.ModelForm):
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
