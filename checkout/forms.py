from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        # Telling the form which model is associated with.
        model = Order
        # And which fields to display.
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    # Overriding the init method which will allow us to
    # customize it quite a bit.
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # First we call the defaul init method to set the
        # form up as it would be by default.
        super().__init__(*args, **kwargs)

        # Placeholders dictionary.
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Autofocus on name field to true.
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # Add star to placeholder of required fields.
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                    self.fields[field].widget.attrs['value'] = ''
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Removing the labels since we now have placeholders.
            self.fields[field].label = False
