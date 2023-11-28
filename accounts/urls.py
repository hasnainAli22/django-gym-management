from django.urls import path
from django.views.generic.base import TemplateView
from accounts.views import *

# Create the patterns
app_name = 'accounts'
urlpatterns = [
    path('signup/',RegisterUserView.as_view(), name='signup'),
    path('member/signup/', RegisterMemberView.as_view(), name='register_member'),
    path('trainer/signup/',RegisterTrainerView.as_view(), name='register_trainer'),
    path('admin/signup/', RegisterAdminView.as_view(), name='register_admin'),
    path('login/', LoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('member/profile/', ProfileUpdatePage.as_view(), name='member_profile'),
    path('trainer/profile/', ProfileUpdatePage.as_view(), name='trainer_profile'),
    path('admin/profile/', ProfileUpdatePage.as_view(), name='admin_profile'),
    path("password_change/", PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/",PasswordChangeDoneView.as_view(),name="password_change_done",),
    path("password_reset/",PasswordResetView.as_view(), name="password_reset"),
    path("password_reset_done/",PasswordResetDoneView.as_view(),name='password_reset_done'),
    path("reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]