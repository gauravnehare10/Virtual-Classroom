from django import forms
from .models import Discussion, Class, Student, User, Instructor, ClassRoom
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my2', 'placeholder': 'Enetr Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my2', 'placeholder': 'Enetr Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my2', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my2', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['bio']

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['comment', 'parent']

class EnrollmentForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset=ClassRoom.objects.all(), label="Select Class")

