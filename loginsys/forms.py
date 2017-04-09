from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    teachers_key = forms.CharField(max_length=30, label='Код преподавателя')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'teachers_key', 'email', 'password1', 'password2',)