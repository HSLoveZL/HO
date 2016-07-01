# myflasky
my flasky - HO 目前部署位置：http://121.40.213.161/

请在项目根目录下创建项目密码配置文件mydata.ini
配置项目包括
[MAIL]
MAIL_USERNAME=***
MAIL_PASSWORD=***
[MySQL]
MySQL_PASSWORD=***
[APP]
SECRET_KEY=***

# 阿里云部署笔记
Flask + uwsgi + nginx
主要参考：
http://www.cnblogs.com/Ray-liang/p/4173923.html?utm_source=tuicool&utm_medium=referral  
http://blog.csdn.net/yuan882696yan/article/details/50196787  
http://juxuan.fu.blog.163.com/blog/static/112129259201411188132562/  
http://www.testercode.com/post/3  
http://duzhipeng.com/pages/150921/  
注意 文章1中错误点：  
1. 安装pip时候要用 `sudo apt-get install python-pip`
2. 在uwsgi的ini文件中 `chdir = /home/www/` 要改成 `chdir = /home/www/my_flask`

# 虚拟环境搭建
参考：
http://www.ittang.com/2014/0720/13403.html
使用virtualenvwrapper
1. Windows：
首先安装virtualenvwrapper：`pip install virtualenvwrapper-win`虚拟环境默认统一安装在`C:\Users\xxx\Envs`下面
然后`mkvirtualenv VirtualenvName`
进入虚拟环境后`pip install -r 项目目录下\requirements.txt`

2. Linux：
参考：
http://virtualenvwrapper.readthedocs.io/en/latest/
http://my.oschina.net/williambao/blog/205311


# 从sqlite转移到Mysql（ubuntu平台）
参考：
http://www.cnblogs.com/wangqingbaidu/p/3241954.html
http://www.cnblogs.com/xiazh/archive/2012/12/12/2814289.html
http://www.111cn.net/database/mysql/44142.htm
1. `sudo apt-get install mysql-server`安装mysql
2. `pip install python-mysqldb` （虚拟环境中） 
如果报错`EnvironmentError: mysql_config not found`
可以安装`apt-get install libmysqlclient-dev`
3. 本地登陆mysql数据库，创建root账户和密码，在登陆过程中如果遇到
`ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password:YES)`
可以试试修改密码`mysqladmin -u root -p password 'newpassword'`
创建本项目需要的数据库`create database myflasky;` 然后退出mysql
在工程中的个人密码配置文件`mydata.ini`中加入MySQL的配置项
4. （虚拟环境中）`python manage.py shell `
`db.create_all()`创建所有的表
`Role.insert_roles()`创建role表中的角色

# 从sqlite转移到Mysql(Windows平台)
和Ubuntu中最大的不同的是解决虚拟环境中没有MySQLdb模块的问题
通过（虚拟环境中）`pip install mysqlclient`解决