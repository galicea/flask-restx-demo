from . import app
import logging
import configparser

from werkzeug.middleware.dispatcher import DispatcherMiddleware

config = configparser.ConfigParser()


def init(log):
  config.read("conf/api.ini")

  app.config['APPLICATON_ROOT'] = '/api'
#  app.wsgi_app = DispatcherMiddleware(simple, {'/api': app.wsgi_app})
  app.config['RESTX_MASK_HEADER']=False
  app.config['RESTX_MASK_SWAGGER']=False
  app.config.setdefault('RESTX_MASK_SWAGGER', True)
  app.config['ORIGIN']=config['app']['origin']
  app.secret_key = config['app']['secret']

  if log:
    logfile = config['app']['logfilename']
    logging.basicConfig(filename=logfile, level=logging.DEBUG)

