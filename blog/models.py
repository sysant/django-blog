from django.db import models
from django.contrib.auth.models import User
from django.utils.functional import cached_property  # 缓存装饰器
from django.template.loader import render_to_string  # 渲染模板


# Create your models here.


class Category(models.Model):
    """ 博客分类模型 """
    name = models.CharField(max_length=32, verbose_name='分类名称')
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name='分类描述')
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """ 文章标签模型 """
    name = models.CharField(max_length=10, verbose_name='标签名称')
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    """ 文章 """
    title = models.CharField(max_length=64, verbose_name='文章标题')
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name='文章描述')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类')
    content = models.TextField(verbose_name='文章详情')
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True, verbose_name='文章标签')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    is_hot = models.BooleanField(default=False, verbose_name='是否热门')   # 手动设置热门
    pv = models.IntegerField(default=0, verbose_name='浏览量')      # 浏览量计数
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Sidebar(models.Model):
    """侧边栏的模型数据  """

    STATUS = (
        (1, '隐藏'),
        (2, '展示')
    )

    DISPLAY_TYPE = (
        (1, "搜索"),
        (2, "最新文章"),
        (3, "最热文章"),
        (4, "最近评论"),
        (5, "文章归档"),
        (6, "HTML")
    )
    title = models.CharField(max_length=50, verbose_name="模块名称")  # 模块名称
    display_type = models.PositiveIntegerField(default=1, choices=DISPLAY_TYPE, verbose_name="展示类型")  # 侧面栏展示内容(搜索框、最新文章等)
    content = models.CharField(max_length=500, blank=True, default='',
                               verbose_name="内容", help_text="如果设置不是HTML类型，可为空")  # 专门给html类型用，其他类型可以为空
    sort = models.PositiveIntegerField(default=1, verbose_name="排序", help_text="序号越大越靠前")
    status = models.PositiveIntegerField(default=2, choices=STATUS, verbose_name="状态")  # 隐藏， 显示状态
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")  # 创建时间

    class Meta:
        verbose_name = "侧边栏"
        verbose_name_plural = verbose_name
        ordering = ['-sort']

    def __str__(self):
        return self.title

    @classmethod  # 类方法装饰器，类方法可以直接调用，不需要实例化
    def get_sidebar(cls):
        return cls.objects.filter(status=2).order_by('-sort')

    @property  # 成为类属性，调用的时不用(),是只读的，用户没办法修改
    def get_content(self):
        if self.display_type == 1:
            context = {}
            return render_to_string('blog/sidebar/search.html', context=context)
        elif self.display_type == 2:
            context = {}
            return render_to_string('blog/sidebar/new_post.html', context=context)
        elif self.display_type == 3:
            context = {}
            return render_to_string('blog/sidebar/hot_post.html', context=context)
        elif self.display_type == 4:
            context = {}
            return render_to_string('blog/sidebar/comment.html', context=context)
        elif self.display_type == 5:  # 文章归档
            context = {}
            return render_to_string('blog/sidebar/archives.html', context=context)
        elif self.display_type == 6:  # 自定义侧边栏
            return self.content  # 在侧边栏直接使用这里的html, 必须使用safe过滤器去渲染html
