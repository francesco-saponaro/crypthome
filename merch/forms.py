from django import forms
from .models import Merch, Category


class ProductForm(forms.ModelForm):

    # This form extends the merch model and all its fields.
    class Meta:
        model = Merch
        fields = '__all__'

    # Override init method to get category friendly names
    # in the form.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Update category field on the form.
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 \
                stripe-style-input'
