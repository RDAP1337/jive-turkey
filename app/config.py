# ===================================================================
# Global Config - app/config.py
# ===================================================================
import os

# dir config
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SCRIPTS_DIR = 'BASE_DIR/../scripts'

# debug on?
DEBUG = True

# csrf config
SECRET_KEY = 'HVzZSAtLXVwZ3JhZGUgdG8gdX'

# sqlalchemy config
SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/db'
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, '../data/db_repository')

# session config
SESSION_COOKIE_SECURE = True
PERMANENT_SESSION_LIFETIME = 3600
SESSION_REFRESH_EACH_REQUEST = True

# bootstrap3 bootswatch themes config
BS3_BOOTSWATCH_THEMES = [
    'amelia',
    'cerulean',
    'cosmo',
    'cyborg',
    'darkly',
    'flatly',
    'journal',
    'lumen',
    'readable',
    'simplex',
    'slate',
    'spacelab',
    'superhero',
    'united',
    'yeti'
]