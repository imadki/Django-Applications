from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django import forms

from accounts.forms import RegistrationForm



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

## =======================================================
#class RegistrationForm(UserCreationForm):
#    email = forms.EmailField(max_length=60,
#                             help_text='Required. Add a valid email address')
#
#    class Meta:
#        model = Account
#        fields = ('email', 'username', 'password1', 'password2',
#                  'last_name', 'first_name')
