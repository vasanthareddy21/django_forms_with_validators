from django import forms

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