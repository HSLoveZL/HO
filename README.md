# myflasky
my flasky


阿里云部署笔记
Flask + uwsgi + nginx
主要参考：
http://www.cnblogs.com/Ray-liang/p/4173923.html?utm_source=tuicool&utm_medium=referral
注意 文章中错误点：
1. 安装pip时候要用 `sudo apt-get install python-pip`
2. 在uwsgi的ini文件中 `chdir = /home/www/` 要改成 `chdir = /home/www/my_flask`