# 用Django搭建简单博客(目前只做基本功能)

> ## 开发环境
    python2.7
    Django1.11.1

> ## 创建项目

```python
django-admin startproject blog
```

> ## 启动项目

```python
python manage.py runserver
```

> ## 创建应用

1、进入项目中manage.py同级目录输入

```python
python manage.py startapp myBlog
```

2、将应用名称添加入setting.py的INSTALLED_APP中

> ## 配置路由

* 在根urls.py中引入include

* 在应用目录下创建urls.py文件

* 根urls.py中url第二个参数改为include('myBlog.urls')

  ```python
  url(r'^index/', include('myBlog.urls'))
  ```

> ## templates

*  在应用目录下创建templates目录，后创建名称与应用相同的子目录

  -myBlog/

  ​	-templates/

  ​		-myBLog/

  ​			index.html

* 在view.py中render()第二个参数加入myBlog前缀

  ```python
  return render(request, 'myBlog/index.html'）
  ```

> ## Models

* 一个Models对应一个数据表

  > 生成数据表

  * 进入manage.py同级目录

  * 准备数据迁移(不加参数则为该项目下所有应用添加数据表)

    ```python
    python manage.py makemigrations app名(可选)
    ```

  * 执行数据迁移

    ```python
    python manage.py migrate
    ```

  * 查询SQL语句

    ```python
    python manage.py sqlmigrate 应用名 文件ID
    ```

    ​

  * 默认数据库为项目根目录下db.splite3

* 创建字段,字段即类的属性

  ```python
  attr = models.CharField(max_length = 64)
  ```

* 页面呈现数据

  > 后台步骤

  * view.py中Import models

    ```python
    articles = models.Article.objects.all()  [.get(pk=1)]
    render(request, page, {'articles' : articles})
    ```

  > 前端步骤

  * 模板可直接使用对象及对象的的“ . ”操作

    ```python
    {{ article.title }}
    ```

> ## 配置Admin

* 创建用户

  ```python
  python manage.py createsuperuser
  ```

* 配置用户

  * 在应用admin.py下引入自身的models模块或里面的模型类

  * 编辑admin.py

    ```python
    admin.site.register(Article)
    ```

  * 修改数据默认显示名称:在Article类下添加一个方法

    ```python
    def __unicode__(self):
    	return self.title
    ```
