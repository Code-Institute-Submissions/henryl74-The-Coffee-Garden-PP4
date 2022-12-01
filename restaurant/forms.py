from django.forms import ModelForm
from django.core import validators
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """
    This class provides a widget for use in the
    booking form. It cretes a better UX when choosing the date
    for the booking.
    """
    input_type = 'date'


class OnlineForm(ModelForm):
    """
    This class is connected with the view
    in order to provide users with the neccessary
    fields for making a booking.
    It also provides the labels and placeholder
    text for each field, as wells as the widgets
    and handles validation where required.
    """
    name = forms.CharField(
        label='Booking Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Booking Name'}),
    )

    phone = forms.IntegerField(
        label='Contact Number',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Contact number'}),
    )

    class Meta:
        """
        This class defines which model to pull the
        fields from.
        """
        model = Booking
        fields = '__all__'
        exclude = ('user', )
        widgets = {
            'date': DateInput()
        }
