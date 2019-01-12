from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone_number', 'city']
        helper = FormHelper()
        helper.form_class = 'form-group'
        helper.layout = Layout(
        Field('first_name', css_class='form-control mt-2 mb-3'),
        Field('address', rows="3", css_class='form-control mb-3'),
        Field('last_name', css_class='form-control mb-3'),
        Field('email', css_class='form-control mb-3'),
        Field('phone_number', css_class='form-control'),
		Field('city', css_class='form-control'),
        ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
    )