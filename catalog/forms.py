from django import forms

from catalog.models import Product, Version
from config import settings


class ProductForm(forms.ModelForm):
    version = forms.ModelChoiceField(queryset=Version.objects.all(), required=False,
                                     empty_label="Выберите версию")

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if set(name.lower().split()).intersection(settings.FORBIDDEN_WORDS):
            raise forms.ValidationError("Ошибка связана с названием продукта")
        else:
            return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if set(description.lower().split()).intersection(settings.FORBIDDEN_WORDS):
            raise forms.ValidationError("Ошибка связана с описанием продукта")
        else:
            return description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('number', 'name', 'is_active')



