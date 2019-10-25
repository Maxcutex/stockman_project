import os

APP_ENV = os.environ.get('APP_ENV', 'development')
if APP_ENV in ('development', 'production', 'testing','staging'):
    print(APP_ENV, "this is the environment")
    exec('from .{} import *'.format(APP_ENV))
