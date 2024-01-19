from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@api.route("/index")
class RootPath(Resource):
    def get(self):
        return {"Hello": "Flask"}
