from django import forms
from .models import Material, Category, Grade

class MaterialForm(forms.ModelForm):
    new_category = forms.CharField(required=False)
    new_grade = forms.CharField(required=False)

    class Meta:
        model = Material
        fields = ['name', 'file', 'url', 'category', 'grade']

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        new_category = cleaned_data.get('new_category')
        grade = cleaned_data.get('grade')
        new_grade = cleaned_data.get('new_grade')

        if category == 'new' and not new_category:
            self.add_error('new_category', 'Please enter a new category name.')

        if grade == 'new' and not new_grade:
            self.add_error('new_grade', 'Please enter a new grade name.')

        return cleaned_data
