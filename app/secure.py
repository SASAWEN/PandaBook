"""
    Created by cala at 2019-10-24
"""
# 生产环境 开发环境 不同
# 机密信息 不需要上传到git

DEBUG = True
# cymysql 数据库驱动
# 实体数据库连接：数据库类型+连接库+用户名+密码+主机，字符编码，是否打印建表细节
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:slgb@localhost:3306/my_panda?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = 'True'

SECRET_KEY = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

# email配置
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'wan_sasa@163.com'
# QQ邮箱->设置->账户->[POP3...]->生成授权码->发送短信->获取授权码
MAIL_PASSWORD = 'wenshasha666'
MAIL_SUBJECT_PREFIX = '[PandaBook]'