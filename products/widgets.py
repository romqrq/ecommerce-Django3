from django.forms.widgets import ClearableFileInput
# The _ means we can call _() as an alias for gettext_lazy()
from django.utils.translation import gettext_lazy as _


# this class inherits the built in one and we can override it
# On Django github we can find these widgets and the way they are setup
class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
