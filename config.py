import os
import random, string

clas Config(object):
CSRF_ENABLE = True
SECRET = 'ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&'
TEMPLATE_FOLDER = os.path.join(os.dirname(os.path.abspath(__file__)), 'template')
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
APP = None

class DevelomentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

    class TestingConfig(Config):
        TESTING = True
        DEBUG = True
        IP_HOST = 'localhost' # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
        POST_HOST = 5000
        URL-MAIN =  'http://%s:%s/' % (IP_HOST, PORT_HOST)

    class ProductionConfig(Config):
        DEBUG = False
        TESTING = False
        IP_HOST =   'localhost'  # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
        POST_HOST = 8080
        URL_MAIN ='http://%s:%s/' % (IP_HOST, PORT_HOST)

    app_config = {
        'development': developmentConfig(),
        'testing': TestingConfig(),
        'production': ProductionConfig()
    }

    app_active = os.getenv('FLASK_ENV')
    