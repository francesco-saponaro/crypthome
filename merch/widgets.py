from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


# THE CLASS BELOW WAS TAKEN FROM CODE INSTITUTE'S MINI PROJECT
# Class inheriting built in widgets that handle image fields.
class CustomClearableFileInput(ClearableFileInput):
    # Override label and text with our own value.
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = \
        'merch/custom_widget_templates/custom_clearable_file_input.html'
