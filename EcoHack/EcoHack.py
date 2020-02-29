from flask import Flask

app = Flask(__name__)

from app.routes import *

if __name__ == '__main__':
    app.run(debug=True, port='5050', host='0.0.0.0')
