# 博客主页面

> ## 模板for循环

```python
{% for article in articles %}
	code
{% end for %}
```

> ## 文章页面

* URL传递参数
  * 参数写在响应函数request后，可以有默认值
  * URL正则表达式



```python
url(r'^article/(?P<id>\d+)/$', views.articleCon)
```
* 超链接

  ```python
  {% url 'blog:articleCon' param %}
  ```

* 添加项目URL的include()第二个参数namespace = 'blog'

  ```python
  url(r'^index/', include('myBlog.urls', namespace = 'blog'))
  ```

* 添加应用URL的url()的第三个参数name = 'articleCon'

  ```python
  url(r'^article/(?P<id>\d+)/$', views.articleCon, name = 'articleCon')
  ```

> ## 博客撰写页面

* 在views.py中编辑相应函数

  * 使用request.POST['参数名']获取表单数据

  * 创建对象

    ```python
    models.Article.objects.create(title=title, content=content)
    ```

* 若表单提交为POST提交，则需在表单内部添加{% csrf_token %}

  ```python
  <form action="" method="post">
  	{% csrf_token %}
  </form>
  ```




# Admin

> ## 创建Admin配置类

```python
class ArticleAdmin(admin.ModelAdmin)
```

* 注册:

  ```python
  admin.site.register(Article, ArticleAdmin)
  ```

> ## 显示其他字段

```python
class ArticleAdmin(Article, ArticleAdmin):
	list_display = ('title', 'content')
```

_list_display同时支持tuple和list_

* 过滤器
  ```
  list_filter = ('release_time', )
  ```