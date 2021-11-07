#inherits from the user cretaion form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# to add another attribute eg: email
class UserRegisterForm(UserCreationForm):

    #default = required to true, left empty
    email = forms.EmailField()

    #gives nested namespace for configurations in one place, form.save into this user model
    class Meta:
        #the form to interact with is User, whenever a from is validates, it will create a user 
        model = User
        #display fields
        fields = ['username', 'email', 'password1', 'password2']