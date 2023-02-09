# Python3 学习

```
// 在脚本顶部添加以下命令让 Python 脚本可以像 SHELL 脚本一样可直接执行
#!/usr/bin/env python3


// 修改脚本权限
chmod +x test.py
```


#### Flask
- 首先要有python和虚拟环境
	+ python环境Apple自带或自己安装
	+ 虚拟环境
		- 安装virtualenv:
			+ pip install --user virtualenv (基于python2.7版本)
			+ pip3 install --user virtualenv(基于python3版本）
		- 创建virtualenv:
			+ virtualenv demo1_env
			+ python -m venv demo1_env(基于python2.7版本)
			+ python3 -m venv demo1_env(基于python3版本）
		- 激活virtualenv:
			+ source demo1_env/bin/activate
		- 关闭virtualenv:
			+ deactivate

- 安装Flask
	+ pip install Flask(基于python2.7)
	+ pip3 install Flask(基于python3)

#### mysql
- [Mac安装mysql](https://cloud.tencent.com/developer/article/1625825)
- 链接mysql: mysql -u root -p
- 查看现有数据库: show databases;
- 建库: create database MyTest;
- 打开某个数据库: use MyTest;
- 显示本库中所有表: show tables;
- 退出exit;




