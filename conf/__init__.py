__version__ = "0.0.1"

from flask import Flask
app=Flask(__name__,
#          static_folder='../static',
#          template_folder='../templates'
         )

from .config import config
from .config import init
#init(True)
init(False)

from .endpoints import define
define()

