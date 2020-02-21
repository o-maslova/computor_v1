from django import forms
from app_logic.parsing import check_input


class InputForm(forms.Form):
    input = forms.CharField(empty_value="Enter your polynomial")

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data['input'])
        is_norm = check_input(cleaned_data['input'])
        if not is_norm:
            raise forms.ValidationError("It is not a polynomial equation!")