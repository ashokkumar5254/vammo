from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns=[
    path('profile_view',views.profile_view,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('signup',views.signup,name='signup'),
    path('password_change/',auth_view.PasswordChangeView.as_view(template_name='password_change.html'),name='password_change'),
    path('password_change_done/',auth_view.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    path('',views.home,name='home'),
    path('logout',auth_view.LogoutView.as_view(template_name='home.html'),name='logout'),
    path('passwordreset/',auth_view.PasswordResetView.as_view(template_name='forgetpassword.html'),name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

]