class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'O\xa8[\xe9l\xd7J7\xdc!\x16\xaa%Q\x8dh1\xdc\x12\x93\xb4\xa1\xff\xc7'  #generated using os.urandom(24)
	SQLALCHEMY_DATABASE_URI = 'sqlite:///sample.db' #should be set to environment variable using os.environ['DATABASE_URI'] for easy migration between dev, test and prod env
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False