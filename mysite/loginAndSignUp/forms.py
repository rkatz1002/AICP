from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from loginAndSignUp.models import UserAdmin
from loginAndSignUp.models import Pessoa

# class SignUpForm(forms.ModelForm):
    
#     class Meta:
#         model = UserAdmin
#         fields = ['id','login', 'senha1', 'senha2']

class PessoaForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Pessoa
        exclude = (
                'email',
                'user_permissions',
                'groups',
                'first_name', 
                'last_name', 
                'is_staff', 
                'is_active',
                'is_superuser',
                'last_login',
                'date_joined'
                )

class PessoaChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Pessoa
        exclude = (
                'email',
                'user_permissions',
                'groups',
                'first_name', 
                'last_name', 
                'is_staff', 
                'is_active',
                'is_superuser',
                'last_login',
                'date_joined'
                )


# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('username', 'email')

# class CustomUserChangeForm(UserChangeForm):

#     class Meta(UserChangeForm):
#         model = CustomUser
#         fields = ('username''