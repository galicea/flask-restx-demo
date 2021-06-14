# Quick start

1) Create the catalog:

```
mkdir demo
cd demo
```
2) Prepare environment (optionally)
```
pip install virtualenv
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
```
3) Clone the project:
```
git clone https://github.com/galicea/flask-restx-demo.git
cd flask-restx-demo
```
4) Install nessesery modules
```
pip install -r requirements.txt
```
5) Create api.ini file:
```
cp conf/api.ini.example conf/api.ini
```
6) Run test:
```
./run_debug
```
See address: 
http://localhost:5000/help

# Simple example
1) Create subdir (ex my)  in directory rest and module module rest/my/my.py:



```py
# coding: utf-8

from flask_restx import Namespace, Resource

ns = Namespace('hello', description='Example')

@ns.route('/world',methods=['GET',])
class ApiHello(Resource):

    def get(self):
      try:
        return {
          'result': 'Hello World',
          'retcode': 200,
        }
      except Exception as e:
       return {
         'result': 'Internal Errror! %s' % e,
         'retcode': 500,
       }
```

2) Add import ns from module above to  rest/\_\_ini\_\_.py:
```py
from .my.my import ns as api_my
```
3) Append api\_ns to definitions in conf/endpoints.py file:

```py
from rest import api_my

from rest import api_my
def define():
  api.add_namespace(api_my)
  ....
```