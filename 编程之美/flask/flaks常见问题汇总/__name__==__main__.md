```python
编写python文件时，一般在入口文件处加上
if __name__ == '__main__':
当脚本文件执行时，就会执行该语句下面的内容，但当该文件作为模块被其他文件导入的时候，下面的文件就不会执行
执行app.run()时，会执行flask自带的服务器，效率很低，在生产环境中一般使用nginx+uwsgi作为服务器
nginx作为前置服务器接受浏览器端的请求
项目上线后，有uwisg加载该文件，没有if __name__ == '__main__'就会同时开启2个服务器，产生矛盾
```

testa.py

```python
a = __name__
print(a) ==> __main__
if __name__ == '__main__'
	print('hello world')
```

testb.py

```python
from testa import a
# 先将testa模块执行一次
__name__
print(a) ==> __name__
```

