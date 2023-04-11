from django import forms

class fmrContacto(forms.Form):

    asunto=forms.CharField(required=True,max_length=80)
    email=forms.EmailField(required=True)
    mensaje=forms.CharField(required=True,widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}), max_length=160)



