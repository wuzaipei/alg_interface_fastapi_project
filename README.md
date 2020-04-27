# alg_interface_fastapi_project
python fastapi 构建一个完整项目框架


# 生成依赖包
pip freeze > requirements.txt

# 安装依赖包
pip install -r requirements.txt

# cmd启动
uvicorn appMain:app --host localhost --port 3344 --reload
