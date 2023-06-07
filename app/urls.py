from django.urls import path,reverse_lazy
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,ChangePasswordForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('carentals',views.carentals,name='carentals'),
    path('booking',views.booking,name='booking'),
    path('profile_submit',views.profile_submit,name='profile_submit'),
    #path('registration',views.registration,name='registration'),
    
    path('findroute',views.findroute,name='findroute'),
    path('profile',views.profile,name='profile'),
    path('history',views.history,name='history'),
    path('route',views.route,name='route'),
    #path('logout',views.login,name='logout'),

    path('accounts/login/', auth_views.LoginView.
         as_view(template_name='login.html', authentication_form=LoginForm),name='login'),
    
    #path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('/logout', auth_views.logout_then_login, name='logout'),
    
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='changepassword.html',form_class=ChangePasswordForm,success_url='/passwordchangedone/'),name='changepassword'),
    #path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.
         as_view(template_name='password_reset.html',
                 form_class=MyPasswordResetForm),name='password-reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.
         as_view(template_name='password_reset_done.html'),
                 name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.
         as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm),
                 name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.
         as_view(template_name='password_reset_complete.html'),
                 name='password_reset_complete'),

    path('registration/', views.RegistrationView.as_view(), name="registration"),


    #path('test',views.test_view,name='test'),
]