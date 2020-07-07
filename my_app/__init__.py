from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from flask_migrate import Migrate

app = Flask(__name__)



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

#*********** SQLAlchemy
db = SQLAlchemy(app)
#*********** flask migrate
migrate = Migrate(app, db)
#*********** CORS con cookies
CORS(app, supports_credentials=True)



#importar el modelo
import my_app.model.models

#db.create_all()

#importar las vistas
import my_app.user.views
import my_app.lawyer.views
import my_app.client.views
import my_app.case.views

