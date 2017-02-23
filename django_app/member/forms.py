from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.forms import ModelForm

from member.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())


# class ProfileImageForm(forms.Form):
#     user_pic = forms.ImageField(widget=forms.ClearableFileInput)

class ProfileImageForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['user_pic']


class SignupForm2(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username']


class SignupForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30, required=False)
    gender = forms.ChoiceField(choices=MyUser.CHOICES_GENDER)
    password1 = forms.CharField(widget=forms.PasswordInput)

    password2 = forms.CharField(widget=forms.PasswordInput)

    nickname = forms.CharField(max_length=15)

    def clean_username(self):
        username = self.cleaned_data['username']
        if MyUser.objects.filter(username=username).exists():
            raise forms.ValidationError('username exists')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        validate_password(password1)
        if password1 != password2:
            raise forms.ValidationError("password1 and password2 does not match")
        return password2

    def create_user(self):
        username = self.cleaned_data['username']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        email = self.cleaned_data['email']
        nickname = self.cleaned_data['nickname']
        gender = self.cleaned_data['gender']
        # if MyUser.objects.filter(username=username).exists():
        #     form.add_error('username', 'username already exist')
        # if password != confirm_password:
        #     form.add_error('password', 'please confirm your password')
        #     # raise forms.ValidationError(
        #     #     "password and confirm_password does not match"
        user = MyUser.objects.create_user(username=username, password=password1)
        user.email = email
        user.gender = gender
        user.nickname = nickname
        user.save()
        return user



# class RegisterForm(ModelForm):
#     class Meta:
#         model = MyUser
#         fields = ['username','password','nickname','email','gender']
#         confirm_password = forms.CharField(widget=forms.PasswordInput())

# username = forms.CharField(max_length=20)
# password = forms.CharField(widget=forms.PasswordInput())
# email = forms.EmailField(blank=True)
# gender = forms.CharField(max_length=1, choices=CHOI)
