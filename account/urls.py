from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path(r'login/', views.user_login, name='user_login'),
    path(r'login/', auth_views.LoginView.as_view(template_name="account/login.html"), name='user_login'),  # 使用Django内置的登录方法
#Django内置的登录方法 LoginView（）函数里有一个
# 参数redirect_field_name=LOGIN_REDIRECT_URL，这就是登录后
# 的重定向设置，这行代码就是我们对这个参数的配置，登录后重定向到/blog/
    path(r'loginout/', auth_views.LogoutView.as_view(template_name="account/logout.html"), name='user_logout'),  # 使用Django内置的登出方法
    path(r'register/', views.user_register, name='user_register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html', success_url='/account/password-change-done/'), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name="account/password_reset_form.html",
             email_template_name="account/password_reset_email.html",
             subject_template_name="account/password_reset_subject.txt",
             success_url="/account/password-reset-done/"),
         name='password_reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html",
                                                     success_url='/account/password-reset-complete/'),
         name="password_reset_confirm"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
path('my-information/', views.myself, name='my_information'),
path('edit-my-information/', views.myself_edit, name="edit_my_information"),
path('my-image/', views.my_image, name="my_image"),
    ]
