from common.common import *
from school.school import School




APP.config['MYSQL_DATABASE_USER'] = 'root'
APP.config['MYSQL_DATABASE_PASSWORD'] = '1234'
APP.config['MYSQL_DATABASE_DB'] = 'test'
APP.config['MYSQL_DATABASE_HOST'] = 'localhost'

MYSQL.init_app(APP)



API.add_resource(School, '/school')


if __name__ == '__main__':
    LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d')
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setFormatter(LOG_FORMAT)
    handler.setLevel(logging.DEBUG)
    APP.logger.setLevel(logging.DEBUG)
    APP.logger.addHandler(handler)


    APP.run()
