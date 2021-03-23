# rank
排行榜服务
### 首先打开配置django setting中的DATABASES，进行相关配置
#### 我用的数据库是mysql，最后两项用户名和密码对应自己的数据库来改
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Rank',
        'PORT':3306,
        'HOST':'127.0.0.1',
        'USER':'root',
        'PASSWORD':'123456'
    }
}

### 之后打开mysql创建数据库  create database Rank charset=utf8;
### 打开目录终端 输入命令 python3 manage.py makemigrations,之后输入python3 manage.py migrate完成数据迁移
### 输入命令python3 manage.py runserver 启动程序
### 输入命令python3 manage.py shell 进入django-shell环境进行orm操作
首先导入数据库模型，然后创建样例
### from test_API.models.py import Info
### Info.objects.create(client=客户端,score=99)


### 浏览器输入http://127.0.0.1:8000/rank/upload/ 输入客户端，提交分数
### 浏览器输入http://127.0.0.1:8000/rank/show 进行相关查询
