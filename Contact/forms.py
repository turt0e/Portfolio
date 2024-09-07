from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Specify the model class here
        fields = ['fullname', 'email', 'subject', 'message']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
        }

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        if not fullname:
            raise forms.ValidationError('This field is required')
        return fullname

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('This field is required')
        return email

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if not subject:
            raise forms.ValidationError('This field is required')
        return subject
