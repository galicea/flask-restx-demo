#!/bin/bash
# coding: utf-8

from . import app
from flask_cors import CORS

# CORS

cors=CORS(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', app.config['ORIGIN'])
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

