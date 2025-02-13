from django.contrib import admin

# Register your models here.

from .models import Category, Post, Tag, Sidebar

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Sidebar)


class PostAdmin(admin.ModelAdmin):
    """ 文章列表显示的字段和过滤器 """

    list_display = ('id', 'title', 'category', 'tags', 'owner', 'is_hot', 'pv', 'pub_date')
    list_filter = ('owner',)
    search_fields = ('title', 'desc')
    list_editable = ('is_hot',)
    list_display_links = ('id', 'title', )

    class Media:
        css = {
            "all": ("ckeditor5/cked.css", ),
        }
        js = (
            'https://cdn.bootcdn.net/ajax/libs/jquery/3.7.1/jquery.js',
            'ckeditor5/ckeditor.js',
            'ckeditor5/translations/zh.js',
            'ckeditor5/config.js',
        )


admin.site.register(Post, PostAdmin)
