import os

APP_ENV = os.environ.get('APP_ENV', 'development')
if APP_ENV in ('development', 'production', 'testing','staging'):
    exec('from .{} import *'.format(APP_ENV))
