from flask import Flask
from flask_cors import CORS
from api.routes.tractoras import tractoras_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(tractoras_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
