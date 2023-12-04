from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, TemplateView, View
from django.contrib.auth import views as authviews
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
# Local imports
User = get_user_model() # get the user model dynamically
from .forms import UserCreationForm, LoginForm, CustomPasswordChangeForm, CustomPasswordResetForm, CustomSetPasswordForm
from .models import UserProfile, UserRole

# Create your views here.
"""
Accounts Views Like Registration, Autherization and Authentication
"""
class RegisterUserView(TemplateView):
    template_name = 'registration/presignup.html'


class RegisterMemberView(View):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form, 'role': 'MEMBER'})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.create(user=user, user_role=UserRole.objects.get(name='MEMBER'), is_approved=True)
            return redirect('accounts:login')
        return render(request, self.template_name, {'form': form, 'role': 'MEMBER'})

class RegisterTrainerView(View):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form, 'role': 'TRAINER'})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.create(user=user, user_role=UserRole.objects.get(name='TRAINER'),name=user.username)
            return redirect('accounts:login')
        return render(request, self.template_name, {'form': form, 'role': 'TRAINER'})

class RegisterAdminView(View):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form, 'role': 'ADMIN'})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.create(user=user, user_role=UserRole.objects.get(name='ADMIN'),name=user.username)
            return redirect('accounts:login')
        return render(request, self.template_name, {'form': form, 'role': 'ADMIN'})


class LoginView(authviews.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return super().form_invalid(form)
    
    def get_success_url(self):
        # Redirect users to their specific profile based on their roles
        user_role = self.request.user.userprofile.user_role.name

        if user_role == 'MEMBER':
            return reverse_lazy('accounts:member_profile')
        elif user_role == 'TRAINER':
            return reverse_lazy('accounts:trainer_profile')
        elif user_role == 'ADMIN':
            return reverse_lazy('accounts:admin_profile')

        # Default redirect if the user role is not recognized
        return reverse_lazy('home')
    
    def get_form(self):
        form=super().get_form()
        form.fields['username'].widget=forms.TextInput(attrs={'class':'form-control form-control-lg','id':'form3Example3','placeholder':'Enter a valid email address'})
        form.fields['password'].widget=forms.PasswordInput({'class':'form-control form-control-lg','id':'form3Example4','placeholder':'Enter password'})

        return form
    
    
    

class LogoutView(authviews.LogoutView):
    template_name = 'registration/logout.html'


"""
Views for profile Management
"""

@method_decorator(login_required, name='dispatch')
class ProfileUpdatePage(UpdateView):
    model = UserProfile
    fields = ['name', 'contact_number', 'preferences', 'gender', 'address', 'profile_picture']
    template_name = 'users/base_profile.html'  # Create a template for rendering the form
    def get_object(self, queryset=None):
        # Return the UserProfile object for the currently logged-in user
        return self.request.user.userprofile

    def get_success_url(self):
        return reverse_lazy('home')
    
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'form-control'})
        form.fields['contact_number'].widget=forms.TextInput(attrs={'class':'form-control'})
        form.fields['preferences'].widget=forms.Textarea(attrs={'class':'form-control'})
        GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        )
        form.fields['gender'] = forms.ChoiceField(
            choices=GENDER_CHOICES,
            label='Gender',
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        form.fields['address'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Put your Address'})
        form.fields['profile_picture'].widget.attrs.update({
        'class': 'form-control-file form-control',
        'type': 'file'
        })
        return form
    

class TestView(View):
    def get(self, request, *args, **kwargs):
        # Print the contents of request.user to the console
        # print("request.user:", request.user.userprofile.userrole)

        # You can also use logging for more structured output
        # import logging
        # logger = logging.getLogger(__name__)
        # logger.debug("request.user: %s", request.user)

        return HttpResponse("Check the console for request.user information.")
    
    

"""
Password Views
"""
class PasswordChangeView(authviews.PasswordChangeView):
    template_name = 'registration/password_change.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    
    
class PasswordChangeDoneView(TemplateView):
    template_name = 'registration/password_change_complete.html'

class PasswordResetView(authviews.PasswordResetView):
    template_name = 'registration/password_reset.html'
    form_class = CustomPasswordResetForm
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('accounts:password_reset_done')


class PasswordResetConfirmView(authviews.PasswordResetConfirmView):
    template_name = 'registration/password-reset-confirm.html'
    form_class = CustomSetPasswordForm


class PasswordResetCompleteView(authviews.PasswordResetCompleteView):
    template_name = 'registration/password-reset-complete.html'
    

class PasswordResetDoneView(authviews.PasswordResetDoneView):
    template_name = 'registration/password-reset-done.html'







    
    