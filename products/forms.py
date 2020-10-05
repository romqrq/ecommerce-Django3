from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # this dunder includes all the fields
        fields = '__all__'
    # imported clearable file widget and replace the image field on the form
    # with the new one which utilises the widget
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
        # This special syntax is called the list comprehension. just a shorthand to create 
        # a for loop that adds items to a list
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # updating the category field on the form.
        self.fields['category'].choices = friendly_names
        # iterate through the rest of these fields and set some classes on them
        # to make them match the theme of the rest of our store.
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'