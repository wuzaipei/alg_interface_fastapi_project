#  -*- coding:utf-8 -*-
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 静态文件路径配置
app.mount("/static", StaticFiles(directory="static"), name = "static")   #  挂载静态文件，指定目录

# 模板文件路径配置
templates = Jinja2Templates(directory="templates")   #  模板目录
