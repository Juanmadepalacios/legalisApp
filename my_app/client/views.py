from my_app import app, db, jsonify
from flask import request
from my_app.model.models import User, Client, Lawyer, Case, Document, Message

@app.route("/client", methods=['GET', 'POST'])
@app.route("/client/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def clients(id=None):
   #get lawyer
   if request.method == "GET":
     pass