# django-blog
基于django和bulma框架开发的个人博客系统


线上环境说明：
alamlinux 9   python3.9  yum安装nginx

1、拉取代码
cd /data/
git clone git@github.com:sysant/django-blog.git

2、安装环境依赖(python安装忽略python3.8 + )
pip install -r requirements.txt
yum install nginx -y

3、数据库初始化
cd django-blog
python manage.py makemigrations users blog
python manage.py migrate

4、创建超级管理员
python manage.py createsuperuser
用户名 (leave blank to use 'root'): admin
电子邮件地址:     ＜－－－－　输入你的邮箱格式的地址
Password:        ＜－－－－按提示输入密码
Password (again): ＜－－－－按提示输入密码
Superuser created successfully.

5、测试访问
cd /data/django-blog
python manage.py runserver 0.0.0.0:8080


6、通过uwsgi启动blog系统
cd /data/django-blog/deploy
uwsgi --ini uwsgi.ini
此时netstat -ntpul 会看到本地侦听了8001端口；端口在uwsgi.ini中配置

7、配置并启动nginx

cat /data/django-blog/deploy/blog.conf
upstream django {
    server 127.0.0.1:8001;
    server 127.0.0.1:8001;
}

server {
 listen 8080;     # 原本应该是80
 server_name _; #i just want to hide domain name..
 charset utf-8;
 client_max_body_size 20M;

 # location 配置请求静态文件多媒体文件。
   location /media  {
       alias  /data/django-blog/media/;
   }
 # 静态文件访问的url
 location /static {
       # 指定静态文件存放的目录
       alias /data/django-blog/static/;  
 }

 location / {
   include /data/django-blog/deploy/params;
   uwsgi_pass django;
 }
}


通过软链接过去
ln -s /data/django-blog/deploy/blog.conf /etc/nginx/conf.d/
重启nginx
systemctl restart nginx

 

8、执行静态文件迁移

 mkdir static
 python manage.py collectstatic

427 static files copied to '/data/django-blog/static'.

 

9、测试查看

http://xxxxxxx:8080/admin 

后台创建文章

并通过http://xxxxxxx:8080访问


#### 相关参考文档

1.  参考视频教程：https://www.bilibili.com/video/BV1iU4y1A7MH/
2.  演示站：http://47.121.194.76:8000/

