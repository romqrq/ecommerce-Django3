from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # this dunder includes all the fields
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)
    # overriding the init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # we want the categories to show up in the form with thei friendly name
        # get all categories
        categories = Category.objects.all()
        # Create a list of tuples of the friendly names associated with their category ids
        # This special syntax is called the list comprehension.
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'