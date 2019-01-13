import os

if os.getenv('OPENSHIFT_REPO_DIR'):
    from .staging import *
elif os.getenv('TRAVIS_CI'):
    from .testing import *
elif os.getenv('HEROKU'):
    from .production import *
else:
    from .development import *