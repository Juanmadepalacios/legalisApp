from my_app import app, db, jsonify
from flask import request
from my_app.model.models import User, Client, Lawyer, Case, Document, Message


#Vistas usuario
@app.route('/')
def user():
   return "HOLA MUNDO"


@app.route('/user/start', methods=['GET', 'POST'])
def usuario_inicio(id=None):
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


@app.route('/user/start/query', methods=['GET', 'POST'])
def usuario_consulta(id=None):
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
#post messages   
   if request.method == "POST":
      messages_date = request.json.get('messages_date', None)
      messages_content = request.json.get('messages_content', None)

      if not messages_date:
         return jsonify({"msg":"date is required"}), 422

      if not messages_content:
         return jsonify({"msg":"message ir required"}), 422

      message = Message()
      message.messages_date = messages_date
      message.messages_content = messages_content

      db.session.add(message)
      db.session.commit()

      return jsonify(message.serialize()), 201

@app.route("/user/start/query/<int:id>", methods=['GET'])
def usuario_consulta2(id=None):
#get messages
   if request.method == "GET":
      if id is not None:
         message = Message.query.get(id)
         if message:
               return jsonify(message.serialize()), 200
         else:
               return jsonify({"msg":"message not found"}), 404
      else:
         message = Message.query.all()
         message = list(map(lambda message: message.serialize(), message))
         return jsonify(message), 200

@app.route('/user/start/query/register', methods=['GET', 'POST'])
def cliente_registro(id=None):
#post client
   if request.method == "POST":
      clients_username = request.json.get('clients_username', None)
      clients_email = request.json.get('clients_email', None)
      clients_password = request.json.get('clients_password', None)
      clients_phone = request.json.get('clients_phone', None)
      clients_rut = request.json.get('clients_rut', None)
      clients_address = request.json.get('clients_address', None)
      clients_profession = request.json.get('clients_profession', None)
      clients_nationality = request.json.get('clients_nationality', None)
      clients_civil_status = request.json.get('clients_civil_status', None)
      clients_avatar = request.json.get('clients_avatar', None)



      if not clients_username:
         return jsonify({"msg":"username is required"}), 422



      client = Client()
      client.clients_username = clients_username
      client.clients_email = clients_email
      client.clients_password = clients_password
      client.clients_phone = clients_phone
      client.clients_rut = clients_rut
      client.clients_address = clients_address
      client.clients_profession = clients_profession
      client.clients_nationality = clients_nationality
      client.clients_civil_status = clients_civil_status
      client.clients_avatar = clients_avatar

      db.session.add(client)
      db.session.commit()

      return jsonify(client.serialize()), 201
      #Falta un get a client


#vista cliente
@app.route('/client/', methods=['GET'])
@app.route("/client/<int:id>", methods=['GET'])
def cliente(id=None):
#get client
   if request.method == "GET":
      if id is not None:
         client = Client.query.get(id)
         if client:
               return jsonify(client.serialize()), 200
         else:
               return jsonify({"msg":"client not found"}), 404
      else:
         client = Client.query.all()
         client = list(map(lambda client: client.serialize(), client))
         return jsonify(client), 200
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
#get case
   if request.method == "GET":
      if id is not None:
         case = Case.query.get(id)
         if case:
               return jsonify(case.serialize()), 200
         else:
               return jsonify({"msg":"case not found"}), 404
      else:
         case = Case.query.all()
         case = list(map(lambda case: case.serialize(), case))
         return jsonify(case), 200





   
