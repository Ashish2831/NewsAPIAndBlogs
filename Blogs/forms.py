from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext as _
from .models import *

class Registration_Form(UserCreationForm):
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Password'}), required=False)
    password2 = forms.CharField(label=_("Confirm Password"), widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Confirm Password'}), required=False)

    def __init__(self, *args, **kwargs):
        super(Registration_Form, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields.get('username').required = False

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        labels = {
            'first_name' : _('First Name'),
            'last_name' : _('Last Name'),
            'email' : _('Email'),
        }

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Username'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'First Name'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Last Name'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : 'Email'}),
        }

        help_texts = {
            'username' : ''
        }

    def clean_username(self):
        inp_username = self.cleaned_data.get('username')
        if len(inp_username.strip()) == 0:
            raise ValidationError(_("Please Enter The Username!!"))
        return inp_username

    def clean_first_name(self):
        inp_first_name = self.cleaned_data.get('first_name')
        if len(inp_first_name.strip()) == 0:
            raise ValidationError(_("Please Enter Your First Name!!"))
        return inp_first_name

    def clean_last_name(self):
        inp_last_name = self.cleaned_data.get('last_name')
        if len(inp_last_name.strip()) == 0:
            raise ValidationError(_("Please Enter Your Last Name!!"))
        return inp_last_name

    def clean_email(self):
        inp_email = self.cleaned_data.get('email')
        validator = EmailValidator(_("Please Provide Valid Email!!"))
        validator(inp_email)
        if User.objects.filter(email = inp_email).exists():
            raise ValidationError(_(f"{inp_email} is Already Exists!!"))
        return inp_email

    def clean_password1(self):
        inp_password1 = self.cleaned_data.get('password1')
        if len(inp_password1) == 0:
            raise ValidationError(_("Please Enter The Password!!"))
        return inp_password1

    def clean_password2(self):
        inp_password2 = self.cleaned_data.get('password2')
        inp_password1 = self.data.get('password1')
        if len(inp_password2) == 0:
            raise ValidationError(_("Please Confirm Your Password!!"))
        if inp_password1 != inp_password2:
            raise ValidationError(_("Password Must Matched!!"))
        return inp_password2
 

class BlogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields.get(field).required = False
        
    class Meta:
        model = Blog
        fields = '__all__'

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Title'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Content'}),
            'user' : forms.Select(attrs={'class' : 'form-control'}),
            'urlToImage' : forms.URLInput(attrs={'class' : 'form-control', 'placeholder' : 'Url To Image'})
        }  
        
    def clean_title(self):
        inp_title = self.cleaned_data.get('title')
        if len(inp_title.strip()) == 0:
            raise ValidationError(_("Please Enter The Title!!"))
        return inp_title

    def clean_content(self):
        inp_content = self.cleaned_data.get('content')
        if len(inp_content.strip()) == 0:
            raise ValidationError(_("Please Enter Content!!"))
        return inp_content

    def clean_user(self):
        inp_user = self.cleaned_data.get('user')
        if inp_user == None:
            raise ValidationError(_("Please Select User!!"))
        return inp_user

    def clean_urlToImage(self):
        inp_urlToImage = self.cleaned_data.get('urlToImage')
        if inp_urlToImage == None:
            raise ValidationError(_("Please Enter Image Url!!"))
        return inp_urlToImage
    