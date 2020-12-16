from django import forms


class ProfileForm(forms.Form):
    nams = forms.CharField(max_length=100, label='名字：')

