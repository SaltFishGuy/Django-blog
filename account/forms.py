from django import forms
from django.contrib.auth.models import User
from .models import *



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="ConfirmPassword", widget=forms.PasswordInput)
    #User数据模型中没有这两个字段，在这里我们新增这两个字段，
    # 如果原数据模型中有这两个字段，则可覆盖。
    # 这就是继承 forms.ModelForm 的原因。
    class Meta:
        model = User
        fields = ("username","email")#表示注册表单中使用了User数据模型中的 username 和 email 字段。

    def clean_password2(self):
        cd = self.cleaned_data#会在调用表单实例对象的 is_valid()方法时被执行。
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("两次输入的密码不匹配")
        return cd['password2']


from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme","photo")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)