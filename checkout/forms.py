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
    # customize it.
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
        for field in self.fields:
            # Add star to placeholder of required fields if not country.
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add regex validation to certain fields.
            if field == 'full_name':
                self.fields[field].widget.attrs['pattern'] = \
                    "(?=^.{0,40}$)^[a-zA-Z-]+\s[a-zA-Z-]+$"
                self.fields[field].widget.attrs['title'] = "Please add Name\
                     and Surname. Ensure only one space between the two."
            if field == 'email':
                self.fields[field].widget.attrs['pattern'] = \
                    "\w+@\w+\.\w{2,10}"
                self.fields[field].widget.attrs['title'] = "Please add \
                    correct email format."
            if field == 'phone_number':
                self.fields[field].widget.attrs['pattern'] = "\d+"
                self.fields[field].widget.attrs['title'] = "Please add phone\
                     number. Only digits allowed."
            if field == 'country':
                self.fields[field].widget.attrs['title'] = "Please select a\
                     country from the list."
            # Add class to all inputs
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Removing the labels since we now have placeholders.
            self.fields[field].label = False
