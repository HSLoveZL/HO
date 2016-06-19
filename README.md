# myflasky
my flasky


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

# 环境搭建
参考：
http://www.ittang.com/2014/0720/13403.html
使用virtualenvwrapper
1. Windows：
首先安装virtualenvwrapper：`pip install virtualenvwrapper-win`虚拟环境默认统一安装在`C:\Users\xxx\Envs`下面
然后`mkvirtualenv VirtualenvName`
进入虚拟环境后`pip install -r 项目目录下\requirements.txt`

2. Linux：
