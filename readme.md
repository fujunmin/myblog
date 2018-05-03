未完，待更新。。。
安装django
#  创建项目
django-admin startproject myblog
#  创建应用
- 打开命令行，进入项目中manage.py同级的目录
- 命令行输入：```   python manage.py startapp blog  ```
- 将该app添加到settings中
admin.py：该应用的后台管理系统配置
apps.py：该应用的一些配置
models.py ：数据模块、使用ORM框架，类似于MVC中的Models
tests.py：自动化测试模块，djando提供了自动化测试功能。在这里编写测试脚本
views.py：执行响应的逻辑代码，代码逻辑处理的主要地点，项目大部分代码在这里编写

# 创建第一个响应
## 1. 编辑blog.views
- 每个响应对应一个函数，函数必须返回一个响应
- 函数必须存在一个参数，一般约定为request
每个响应（函数）对应一个URL
## 2. 配置URL
- 编辑urls.py
    - 每个URL都以url的形式写出来
    - url函数放在urlpatterns列表中
    - url函数三个参数：URL（正则），对应方法，名称

-------
# Templates介绍
**什么是Templates**
HTML文件：
> 使用了Django模板语言（Django Templates Language，**DTL**）可以使用第三方模板（如jinjia2）

# 开发第一个Templates
**步骤**
- 在app的根目录下创建名叫Templates的目录
- 在该目录下创建HTML文件
- 在views.py中返回render()

#DTL初步使用
- render（）函数中支持一个**dict类型**参数
- 该字典是后台传递到模板的参数，**键为参数名**
- 在模板中使用**{{参数名}}**来直接使用

#新建一个应用blog2，和blog一样，如何解决Templates的冲突问题
- 在templates目录下创建以**APP名为名称的目录**
- 将**html文件**放入到新创建的目录下

-----
# Models介绍
## django中的models是什么？
通常，**一个model**对应数据库中的**一张数据报表**
django中models以**类**的形式表现
它包含了一些**基本字段**以及数据的**一些行为**

##ORM
对象关系映射，实现了对象和数据库之间的映射，隐藏了数据访问的细节，不需要编写sql语句
##步骤
- 在应用根目录下创建models.py，并引入models模块
- 创建类，继承models.Model，该类即是一张数据表
- 在类中创建字段
    >字段创建

    - 字段即类里面的属性（变量）
    - attr = models.CharField(max_length=64)

#生成数据表
步骤：
- 命令行进入manage.py统计目录
- 执行python manage.py makemigrations app名（可选）
- 再执行python manage.py migrate
## 查看
- django会在app/migrations/目录下生成移植文件
- 执行python manage.py sqlmigrate 应用名 文件id   查看sql语句
- 默认sqlite3的数据库在项目根目录下db.sqlite3
```
fujunmindeMacBook-Pro:myblog fujunmin$ python manage.py sqlmigrate bblog 0001
System check identified some issues:

WARNINGS:
?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace
CommandError: App 'bblog' does not have migrations
fujunmindeMacBook-Pro:myblog fujunmin$ python manage.py sqlmigrate blog 0001
System check identified some issues:

WARNINGS:
?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace
BEGIN;
--
-- Create model Article
--
CREATE TABLE "blog_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(32) NOT NULL, "content" text NULL);
COMMIT;
fujunmindeMacBook-Pro:myblog fujunmin$

```
备注：0001指的就是


##查看并编辑db.sqlite3
- 使用第三方软件：SQLite Expert Personal
- 轻量级，完全免费

##呈现页面数据
- **后台步骤**
    - views.py中import models
    - article = models.Article.objects.get(pk=1) # 获取后台数据
    - render(request,page,{'article':article })   # 将数据传递到前端page页面

- **前端步骤**
    - 模板可直接使用对象以及对象的“.”操作  {{article.title}}

--------
#什么是Admin？
admin是django自带的一个工鞥呢强大的自动化数据管理界面
被授权的用户可直接在admin中管理数据库
django提供了许多针对admin的定制功能

#配置Admin
##创建用户  ```python manage.py createsuperuser```   创建超级用户
admin/fujunmin
- 修改语言：在settings.py下修改成 LANGUAGE_CODE = 'zh_Hans'    即可

##配置应用
- 在应用admin.py中引入自身的models模板（或里面的模型类）
- 编辑admin.py：admin.site.register(models.Article)


#修改数据默认显示名称（现在显示的是：Article object）

步骤：
- 在Article类下添加一个方法
- 根据python版本选择__str__(self)或__unicode__(self)
- return self.title

-----------
#完善博客

#博客页面设计：
##页面概要
- 博客主页面
- 博客文章内容页面
- 博客撰写页面

###博客主页面：
####主页面内容
- 文章标题列表，超链接
- 发表博客按钮（超链接）
####列表编写思路
- 取出数据库中所有文章对象
- 将文章对象们打包成列表，传递到前端
- 前端页面把文章以比包体超链接的形式逐个列出
####模板for循环
```
{%for xx in xxs}
HTML语句
{% endfor %}
```
注意：和之前调用对象时候用的是{{}}

--------------

# 博客文章页面
## 页面内容：
- 标题
- 文章内容
- 修改文章按钮（超链接）

# URL传递参数
- 参数写在响应函数中request后，可以有默认值
- URL正则表达式：r'^article/(?P<article_id>[0-9]+)$
- URL正则中的组名**必须和参数名一致**

---

#django模板中的超链接配置

#django中的超链接
##超链接目标地址
- href后面的**目标地址**
- template中可以用 **“ {% url 'app_name:url_name' param %} ”**
- 其中**app_name** 和 **url_name**都在**url**中配置
##再配URL
- url函数的名称参数
- 跟urls，写在include（）的第二个参数位置，namespace='blog',  ```url(r'^blog/', include('blog.urls',namespace='blog'))```
- 应用下则写在url（）的第三个参数位置，name='article'

主要取决于是否使用include（）引用了另一个url配置文件

-----

#博客撰写页面
##页面内容
- 标题编辑栏
- 文章内容编辑区域
- 提交按钮

##编辑响应函数
- 使用**request.POST['参数名']**获取表单数据
- models.Article.objects.create(title,content) 创建对象





