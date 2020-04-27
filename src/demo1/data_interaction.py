#  -*- coding:utf-8 -*-

from fastapi import  Request,APIRouter
from system_file.app_config import templates
from starlette.responses import RedirectResponse
from system_file.databases_config import db
from data_model.dtModel import User,Item
app_test = APIRouter()



@app_test.get("/data")
async def  read_data(request:Request,data:str):
    # data = '八戒你瘦了！'
    return templates.TemplateResponse("index.html", {"request": request, "title": data,"imgurl":"/static/miss.png"})
# http://127.0.0.1:11510/data?data="八戒你瘦了！"



# @app.get("/data")
# async def read_data():
#
#     return "八戒你瘦了！,hello word!"


@app_test.get("/")
async def read_data(request:Request):

    # 查询数据
    res = db.query(User).filter(User.id==1).all()
    # print(dir(res[0]))
    # print(res[0].__dict__["username"])
    # print(666)

    uname = res[0].username
    return RedirectResponse("/test/data?data={}".format(uname))



# js请求注意：js对象转json数据:  JOSN.stringify();json数据转js对象: JSON.parse();
@app_test.post("/jsoned")
async def get_json(item:Item):
    df = {"title":"八戒你瘦了!","lst":[1,2,3,4,5]}
    # print(item.df)
    print(item.dict()["df"]["dt1"][:])
    return {"data":df}
