from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, EmailVerifyRecord
# Register your models here.

# 看到这个用户选项就是官方默认通过UserAdmin这个类注册到后台的，那么我们也引进来，后边继承这个类
from django.contrib.auth.admin import UserAdmin

# 取消注册原有的用户，
admin.site.unregister(User)
# 定义关联对象的样式，StackedInline为纵向排列每一行，TabularInline为并排排列


class UserProfileInline(admin.StackedInline):
    model = UserProfile


# 关联UserProfileAdmin类和UserAdmin类，这样我们就可以在用户页面中添加用户信息了
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]


# 注册User模型
admin.site.register(User, UserProfileAdmin)


@admin.register(EmailVerifyRecord)    # 等同 admin.site.register(EmailVerifyRecord)
class Admin(admin.ModelAdmin):
    list_display = ('code',)