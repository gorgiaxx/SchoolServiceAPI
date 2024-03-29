# 校园服务接口

[apiary接口文档](http://docs.schoolservice.apiary.io/)

## 实现功能：

* cas跳转登录智慧交大和教务系统

* 用户模型

* 获取所有15级及以后班级成员名单

* 用户姓名返回和验证接口

* 用户密码验证接口

* 用户信息接口

* 15级成绩,课表，考试安排查询接口

* 14级成绩查询接口

## TODO

* 14级课表, 考试安排接口

* 查饭卡，图书馆接口

* 查询信息缓存

## 部署方法
``请注意系统权限``

``` 
 > python版本
 
    python -V
 
    python 2.7
    
 > 安装mysql
    yum install python-devel
    yum install mysql
    yum install mysql-devel
    yum install gcc gcc-devel
    
 > 创建数据库
    mysql -u root -p
    create database ss_ecjtu_tech character set utf8;
    修改mysql的my.cnf
    
    [client]
    default-character-set=utf8
    
    [mysqld]
    character-set-server=utf8
    
    [mysql]
    no-auto-rehash
    default-character-set=utf8
    
    > service mysql restart
    
 > 安装python-pip
 
    yum install python-pip
 
 > pip install virtualenv
 
 > virtualenv env
 
 > source env/bin/activate
 
 > pip install -r requirements.txt
 
 > 安装node服务 :
   
    node -v
 
    v7.1.0

> cp config.py.example config.py

> vim config.py

> cd node_server;
    
    npm install -g pm2;
    
    pm2 start app.js --name ss_ecjtu_tech

> cd ..;python deploy.py

> gunicorn -c gunicorn.conf app:app &
```

```option: 使用supervisor```

```
> pip install supervisor

> echo_supervisord_conf

> echo_supervisord_conf > /etc/supervisord.conf

> mkdir /etc/supervisor.d

> echo "[include]" >> /etc/supervisord.conf

> echo "files = /etc/supervisor.d/*.conf" >> /etc/supervisord.conf

> cp ss_supervisor.conf /etc/supervisor.d

> 修改ss_supervisor.conf配置

> supervisord -c /etc/supervisord.conf

> supervisorctl start ss_ecjtu_tech
```

``option: 开机自动启动 Supervisord``

> centos7.2
```
echo "/usr/bin/supervisord -c /etc/supervisord.conf" /etc/rc.d/rc.local
```
