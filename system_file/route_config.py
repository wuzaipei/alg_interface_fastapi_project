# conding:utf-8

from system_file.app_config import app
import src.demo1.data_interaction as  data_interaction

app.include_router(router=data_interaction.app_test,prefix="/test")