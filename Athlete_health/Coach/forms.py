from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CoachAuthentication(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not hasattr(user, 'CoachLogin'):
            raise forms.ValidationError('This user is not a Coach')
