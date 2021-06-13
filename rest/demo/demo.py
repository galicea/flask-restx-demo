# coding: utf-8

from flask_restx import Namespace, Resource, reqparse, fields, cors
from flask_mail import Message
from flask_mail import Mail
from conf import app

ns = Namespace('demo', description='Example')

#@cross_origin()
@ns.route('/demo1/<par1>',methods=['GET',])
@ns.param('par1','result = 3*par1')
class ApiContacts(Resource):

    @ns.doc('ApiDemo1')
    def get(self,par1):
      try:
        result=par1*3
        return {
          'result': 'Result: %s' % result,
          'retcode': 200,
        }
      except Exception as e:
       return {
         'result': 'Internal Errror! %s' % e,
         'retcode': 500,
       }

#@cross_origin()
@ns.route('/demo2',methods=['POST',])
@ns.param('par2','result = par2',_in='formData')
class ApiEcho(Resource):

    @ns.doc('ApiDemo2')
    def post(self):
      parser = reqparse.RequestParser()
      parser.add_argument('par2', required=True, location='form')
      try:
        args = parser.parse_args()
        (par2,) = (args['par2'], )
      except Exception as e:
        return {
          'result': 'Parameters! %s' % e,
          'retcode': 400,
        }
      try:
        return {
          'result': 'Result: %s' % par2,
          'retcode': 200,
        }
      except Exception as e:
       return {
         'result': 'Internal Errror! %s' % e,
         'retcode': 500,
       }
