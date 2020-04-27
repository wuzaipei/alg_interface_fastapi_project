# condig:utf-8
from datetime import datetime

from typing import List,Set,Dict
from pydantic import  BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from system_file.databases_config import Base

# 创建数据模型
class Item(BaseModel):
    df: Dict


class User(Base):
    __tablename__ = 'userinfo'
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    role = Column(String(100) )
    password_hash = Column(String(100))
    head_img = Column(String(100))
    # create_time  = Column(DateTime,default=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.username


class atc(Base):
    __tablename__ = 'atc'
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    role = Column(String(100) )
    password_hash = Column(String(100))
    head_img = Column(String(100))
    # create_time  = Column(DateTime,default=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.username