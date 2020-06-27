from my_app import app, db, jsonify
from flask import request
from my_app.model.models import User, Client, Lawyer, Case, Document, Message


#Vistas usuario
@app.route('/')
def user():
   return "HOLA MUNDO"


@app.route('/user', methods=['GET', 'POST'])
@app.route("/user/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def users(id=None):
   #get user
   if request.method == "GET":
      if id is not None:
         user = User.query.get(id)
         if user:
               return jsonify(user.serialize()), 200
         else:
               return jsonify({"msg":"user not found"}), 404
      else:
         user = User.query.all()
         user = list(map(lambda user: user.serialize(), user))
         return jsonify(user), 200
   
   #post user
   if request.method == "POST":
      users_name = request.json.get('users_name', None)
      users_issue_subject = request.json.get('users_issue_subject', None)
      users_issue_description = request.json.get('users_issue_description', None)

      if not users_name:
         return jsonify({"msg":"name is required"}), 422

      if not users_issue_subject:
         return jsonify({"msg":"subject is required"}), 422

      if not users_issue_description:
         return jsonify({"msg":"description is required"}), 422
         
      user = User()
      user.users_name = users_name
      user.users_issue_subject = users_issue_subject
      user.users_issue_description = users_issue_description

      db.session.add(user)
      db.session.commit()

      return jsonify(user.serialize()), 201


      if request.method == 'PUT':
         pass

      if request.method == 'DELETE':
         pass





   
