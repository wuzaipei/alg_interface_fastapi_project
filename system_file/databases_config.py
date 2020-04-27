# conding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
pymysql.install_as_MySQLdb()

databaseHost = '127.0.0.1'
databasePort = 3306
database = 'jgotest'
username = 'root'
password = '123456'

# 创建数据库连接URI
SQLALCHEMY_DATABASE_URL = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(username,password,databaseHost,databasePort,database)
 # ?charset=utf8

# 初始化
engine = create_engine(
    SQLALCHEMY_DATABASE_URL #,connect_args={"check_same_thread":False}
)

# 创建DBSession类型
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基类 用于继承  也可以放到初始化文件中
Base = declarative_base()

# 获取数据库会话，用于数据库的各种操作
def get_db():
    return SessionLocal()

db = get_db()
