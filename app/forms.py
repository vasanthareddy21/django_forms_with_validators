from django import forms
from django.core import validators

def check_for_v(value):
    if value[0]=='v':
        raise forms.ValidationError('started with v')

def check_for_length(value):
    if len(value)<5:
        raise forms.ValidationError( 'length is < 5')

class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_v,check_for_length])
    Sage=forms.IntegerField()
    Sid=forms.IntegerField()
    Semail=forms.EmailField(validators=[check_for_v])
    Remail=forms.EmailField()
    mobile=forms.CharField(min_length=10,max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def clean(self):
        s=self.cleaned_data['Semail']
        r=self.cleaned_data['Remail']
        if(s!=r):
            raise forms.ValidationError('emails are not matched')

    def clean(self):
        a=self.cleaned_data['Sage']
        if(a<13):
            raise forms.ValidationError('age is < 13')
