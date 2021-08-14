from django import forms
from .models import UserProfile


# THIS FORM WAS TAKEN FROM CODE INSTITUTE'S MINI PROJECT
class UserProfileForm(forms.ModelForm):
    class Meta:
        # Telling the form which model is associated with.
        model = UserProfile
        # Render all fields except user field, since that
        # should never change.
        exclude = ('user',)

    # Overriding the init method which will allow us to
    # customize it.
    # Add placeholders and classes, remove auto-generated
    # labels and set autofocus on first field.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Placeholders dictionary.
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Autofocus on phone number field to true.
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        # Add placeholder.
        for field in self.fields:
            if field != 'default_country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 \
                stripe-style-input'
            # Removing the labels since we now have placeholders.
            self.fields[field].label = False
