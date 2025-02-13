from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=32, widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': '用户名/邮箱'
    }))
    password = forms.CharField(label='密  码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '密码'
    }))

    # 自定义验证规则
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username == password:
            raise forms.ValidationError("用户名和密码不能相同!")
        return password


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='邮箱', max_length=32, widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': '用户名/邮箱'
    }))
    password = forms.CharField(label='密  码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '密码'
    }))
    password2 = forms.CharField(label='再次输入密码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '再次输入密码'
    }))

    class Meta:
        # 允许编辑的字段
        model = User
        fields = ['email', 'password']

    def clean_email(self):
        """验证用户是否已经存在"""
        email = self.cleaned_data.get('email')
        user_exists = User.objects.filter(email=email).exists()

        if user_exists:
            raise forms.ValidationError("该用户已存在!")
        return email

    def clean_password2(self):
        """ 验证两次密码是否一致 """
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("两次密码不一致!")
        return password2


class ForgetPwdForm(forms.Form):
    """ 填写email表单 """
    email = forms.EmailField(label='请输入注册邮箱', min_length=4, widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': '用户名/邮箱'
    }))


class ModifyPwdForm(forms.Form):
    """ 修改密码表单 """
    password = forms.CharField(label='输入新密码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '新密码'
    }))


class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ('email',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('nickname', 'desc', 'gexing', 'birthday', 'gender', 'address', 'image')
