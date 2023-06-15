from django import forms

class InputForm(forms.Form):
    name=forms.CharField(label='NAME', max_length=200,widget=forms.TextInput(attrs={'class':'form-control','id':'name'}))
    email=forms.EmailField(label='EMAIL', max_length=200,widget=forms.TextInput(attrs={'class':'form-control','id':'email'}))
    subject=forms.CharField(label='SUBJECT', max_length=200,widget=forms.TextInput(attrs={'class':'form-control','id':'subject'}))
    msg=forms.CharField(label='MESSAGE', max_length=5000, widget=forms.Textarea(attrs={'class':'form-control'}))

