from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Comment
from .models import Post, Tag
from taggit.forms import TagWidget

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

         # Custom validation for content field
        def clean_content(self):
            content = self.cleaned_data.get('content')
            if len(content) < 5:
                raise forms.ValidationError("The comment is too short! Please provide more details.")
            return content
        
class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset = Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={'class': 'form-control'}),
        }

    # TagWidget()