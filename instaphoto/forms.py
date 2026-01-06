from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        # Add Bootstrap classes to all fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter your {field}'
            })

        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-Enter your password'


    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('email' ,'username','password1', 'password2', )

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter your {field.label.lower()}'
            })
            
        # Specific placeholders
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your password'
    
    class Meta:
        model = User
        fields = ('username','password', )

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'pub_date']
        labels = {
            'caption': '',
            'post_image':'',
        }
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "What's on your mind"}),
           
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Write a comment ..."}), 
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        

