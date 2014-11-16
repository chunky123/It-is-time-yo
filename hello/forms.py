from django import forms
import datetime

class NameForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'YO Username', 'size' : '30px', 'required' : 'required' }), label='', max_length=128, required=True)
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'YO Message', 'size' : '30px', 'required' : 'required' }), label='', max_length=400, required=True)
    hours = forms.ChoiceField(choices=[(x, x) for x in range(0, 23)],required=True)
    minutes = forms.ChoiceField(choices=[(x, x) for x in range(0, 59)], required= True)