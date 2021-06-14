#Quick start

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