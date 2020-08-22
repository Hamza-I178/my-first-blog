from django import forms

from .models import Post
from .models import CV
from .models import Public_CV

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('email', 'phone', 'address', 'education', 'work_experience', 'interests',)

class Public_CVForm(forms.ModelForm):

    class Meta:
        model = Public_CV
        fields = ('title', 'name', 'email', 'phone', 'address', 'education', 'work_experience', 'interests',)