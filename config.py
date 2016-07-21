import os
import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))

cf = ConfigParser.ConfigParser()
cf.readfp(open('mydata.ini'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or cf.get("APP", "SECRET_KEY")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = cf.get("MAIL", "MAIL_USERNAME")
    MAIL_PASSWORD = cf.get("MAIL", "MAIL_PASSWORD")

    HO_MAIL_SUBJECT_PREFIX = '[HO]'
    HO_MAIL_SENDER = '857018659@qq.com'
    HO_ADMIN = 'wcbieyuan@gmail.com'
    HO_POSTS_PER_PAGE = 20
    HO_FOLLOWERS_PER_PAGE = 50
    HO_COMMENTS_PER_PAGE = 30

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:%s@localhost/myflasky' % cf.get("MySQL", "MySQL_PASSWORD")


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
