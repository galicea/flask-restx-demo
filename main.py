#!/usr/bin/env python3
# coding: utf-8
# authors: Jerzy Wawro
# (C) Galicea 2021
from conf import app

import os,sys
sys.path.append(os.path.dirname(sys.argv[0]))


debug=True
if __name__ == '__main__':
  app.run(debug=debug,
         host='0.0.0.0', 
         port=5000, 
         threaded=True)
