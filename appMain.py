# conding:utf-8
import uvicorn
from system_file.app_config import app
from system_file.route_config import *
from system_file.config import *
from system_file.databases_config import engine
# 导入数据模进行创建
from data_model.dtModel import *


Base.metadata.create_all(bind=engine)

# cmd启动
# uvicorn appMain:app --host localhost --port 3344 --reload

# if  __name__  ==  '__main__':
#         uvicorn.run(app, host = host, port = port)

