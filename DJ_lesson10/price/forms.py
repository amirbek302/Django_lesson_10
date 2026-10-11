from django import forms


class PriceForm(forms.Form):
    car_model = forms.CharField(max_length=100, widget=forms.TextInput())
    car_description = forms.CharField(max_length=100, widget=forms.TextInput())
    car_make = forms.CharField(max_length=100, widget=forms.TextInput())
    car_image = forms.URLField(widget=forms.URLInput())