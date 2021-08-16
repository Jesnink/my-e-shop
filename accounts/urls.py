from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.urls import path
from accounts import views
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm,PasswordChangeForm,PasswordResetForm
urlpatterns = [
    path('login/',auth_views.LoginView.as_view (template_name='login.html',authentication_form=LoginForm), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='login') , name="logout"),
    path('register/',views.customerregistrationView.as_view(), name="customerregistration"),
    path('passwordchange/',auth_views.PasswordChangeView.as_view (template_name='changepassword.html',form_class=PasswordChangeForm), name="changepassword"),
    path('password_change_done/',auth_views.PasswordChangeView.as_view (template_name='passwordchangedone.html'), name="password_change_done"),
    path('password_reset/',auth_views.PasswordResetView.as_view (template_name='password_reset.html',form_class=PasswordResetForm), name="passwordreset"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view (template_name='password_reset_confirm.html',form_class=SetPasswordForm), name="password_reset_confirm"),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view (template_name='passwordresetdone.html'), name="password_reset_done"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view (template_name='passwordresetcomplete.html'), name="password_reset_complete"),
]