from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
from app import views

import os
from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)

Bootstrap(app)

from views import *

if __name__ == "__main__":
 port = int(os.environ.get("PORT", 5000))
 app.run(host='0.0.0.0', port=port)