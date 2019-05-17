```
1.变量定义
	{{name}}
2.变量可以使用过滤器进行修改(|)
	注意safe过滤器的使用，Jinja2会转义所有变量
	例如：'<h1>Hello</h1>' 
	显示为：'&lt;h1&gt;Hello&lt;/ h1&gt;'
	添加safe标签后：变成 带有格式的显示
	不要在不可行的值上使用safa标签
3、控制结构
	1.if
        {% if xx %}
        {% else %}
        {% endif %}
    2.for
        {% for comment in comments %}
            <li>{{ comment }}</li>
        {% endfor %}
    3.宏【类似函数】一般放在单独的文件中进行导入
        {% macro render_comment(comment) %}
            <li>{{ comment }}</li>
        {% endmacro %}
        例:
        {% import 'macros.html' as macros %}
        	{{ macros.render_comment(comment) }}
    4.模板继承
    	1.定义模板
            {% block xx %}
            {% endblock %}
        2.继承模板
        	{% extends 'xx.html' %}
        	# 重新定义基模板中的内容；而使用super()后，可以引用同名基模板中的内容
        	{% block xx %}
        		{{ super() }}
        	{% endblock %}
```

```
Bootstrap模块的使用
1、导入
    from flask_bootstrap import Bootstrap
    # ...
    bootstrap = Bootstrap(app)
使用注意：
	有些区块是Flask-Bootstrap 自用的，如果直接覆盖可能会导致一些问题
	例如：Bootstrap的CSS和JS文件在styles和scripts区块中定义,如果需要对其进行添加新的内容，需要使用super()函数
	{% block scripts %}
		{{ super() }}
		# 添加的新属性
		<script type="text/javascript" src="my-script.js"></script>
	{% endblock %}

```

```
Bootstrap的常见标签
    doc:整个HTML文档
    html_attribs:<html>标签的属性
    html：<html>标签内容
    head：<head>标签的内容
    title:<title>标签的内容
    metas:一组<meta>标签
    styles:CSS声明
    body_attribs:<body>标签的属性
    body:<body>b标签的内容
    navbar:用户定义的导航栏
    content:用户定义的页面内容
    scripts：文档底部的JavaScript声明
```

```
链接
http://localhost:5000/
url_for()
# 对应用内不同路由的链接
url_for('index') ==> 得到视图函数index的相对地址'/'
# 在浏览器之外使用的链接
url_for('index',_external=True) ==> 得到绝对地址http://localhost:5000/
链接静态文件
# 在static文件夹下，查找favicon.ico文件，得到的为相对路径
url_for('static',filename='favicon.ico')
```

```
静态函数
例如定义收藏夹图标
{% block head %}
	{{ super() }}
<link rel="shortcut icon" href="{{ url_for('static',filename='favicon.ico') }}" type="image/x-icon">
<link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}"
    type="image/x-icon">
{% endblock %}

```

```
补充
图标文件（favicon.ico）上传到网站所在的服务器的根目录下，必须是16*16大小的图标文件。
在<head></head>之间添加
<link rel="icon" href="favicon.ico" >:允许网络设计人员添加任何支持的图像格式的favicon
# 变成16*16大小文件
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
# 使用GIF
<link rel="icon" href="animated_favicon.gif" type="image/gif" >
# 使用PNG
<link rel="Bookmark" href="favicon.ico">

```

```
Flask-Moment本地化时间
flask-moment
1、导入
    from flask_moment import Moment
    moment = Moment(app)
注意：该扩展需要引入jQuery.js 和 Moment.js库
该示例中：Bootstrap已经引入jQuery.js，只需要引入Moment.js就可以
例：注意，该模块需要添加到子模块中，而不是base基模块
    {% block scripts %}
        {{ super() }}
        {{ moment.include_moment() }} # 引入Moment.js库
        {{ moment.locale('zh-cn') }}  # 将Moment本地化
    {% endblock %}
```

