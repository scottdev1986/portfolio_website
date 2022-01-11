from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):
    widgets = {
        'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}),
        'from_email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Email'}),
        'subject' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}),
        'message' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'}),
    }

    name = forms.CharField(label="",widget=widgets.get('name') ,required=True)
    from_email = forms.EmailField(label="",widget=widgets.get('from_email') ,required=True)
    subject = forms.CharField(label="",widget=widgets.get('subject') ,required=True)
    message = forms.CharField(label="",widget=widgets.get('message') ,required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    