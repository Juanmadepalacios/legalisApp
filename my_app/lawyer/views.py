from my_app import app, db, jsonify
from flask import request
from my_app.user.model.models import User, Client, Lawyer, Case, Document, Message

#vistas abogado
@app.route("/lawyer/register", methods=['GET', 'POST'])
@app.route("/lawyer/register/<int:id>", methods=['GET'])
def abogado_registro(id=None):
#post lawyer
   if request.method == "POST":
      lawyers_name = request.json.get('lawyers_name', None)
      lawyers_password = request.json.get('lawyers_password', None)
      lawyers_email = request.json.get('lawyers_email', None)
      lawyers_rut = request.json.get('lawyers_rut', None)
      lawyers_phone = request.json.get('lawyers_phone', None)
      lawyers_field = request.json.get('lawyers_field', None)
      lawyers_title = request.json.get('lawyers_title', None)
      lawyers_file_speciality = request.json.get('lawyers_file_speciality', None)
      lawyers_bank = request.json.get('lawyers_bank', None)
      lawyers_account = request.json.get('lawyers_account', None)
      lawyers_bank_number = request.json.get("lawyers_bank_number", None)
     
      if not lawyers_name:
         return jsonify({"msg":"name is required"}), 422

      if not lawyers_password:
         return jsonify({"msg":"password is required"}), 422

      if not lawyers_rut:
         return jsonify({"msg":"rut is required"}), 422

      if not lawyers_field:
         return jsonify({"msg":"field is required"}), 422

      if not lawyers_title:
         return jsonify({"msg":"title is required"}), 422

      if not lawyers_bank:
         return jsonify({"msg":"bank is required"}), 422

      if not lawyers_account:
         return jsonify({"msg":"account is required"}), 422

      if not lawyers_bank_number:
         return jsonify({"msg":"bank number is required"}), 422

      lawyer = Lawyer()
      lawyer.lawyers_name = lawyers_name
      lawyer.lawyers_password = lawyers_password
      lawyer.lawyers_email = lawyers_email
      lawyer.lawyers_rut = lawyers_rut
      lawyer.lawyers_phone = lawyers_phone
      lawyer.lawyers_field = lawyers_field
      lawyer.lawyers_title = lawyers_title
      lawyer.lawyers_file_speciality = lawyers_file_speciality
      lawyer.lawyers_bank = lawyers_bank
      lawyer.lawyers_account = lawyers_account
      lawyer.lawyers_bank_number = lawyers_bank_number 
      
      db.session.add(client)
      db.session.commit()

      return jsonify(client.serialize()), 201
#get lawyer
   if request.method == "GET":
      if id is not None:
         lawyer = Lawyer.query.get(id)
         if lawyer:
               return jsonify(lawyer.serialize()), 200
         else:
               return jsonify({"msg":"lawyer not found"}), 404
      else:
         lawyer = Lawyer.query.all()
         lawyer = list(map(lambda lawyer: lawyer.serialize(), lawyer))
         return jsonify(lawyer), 200

@app.route("/lawyer/profile/lawyer", methods=['GET'])
@app.route("/lawyer/profile/lawyer/<int:id>", methods=['GET'])
def abogado_perfil_abogado(id=None):
#get lawyer
   if request.method == "GET":
      if id is not None:
         lawyer = Lawyer.query.get(id)
         if lawyer:
               return jsonify(lawyer.serialize()), 200
         else:
               return jsonify({"msg":"lawyer not found"}), 404
      else:
         lawyer = Lawyer.query.all()
         lawyer = list(map(lambda lawyer: lawyer.serialize(), lawyer))
         return jsonify(lawyer), 200

@app.route("/lawyer/profile/user", methods=['GET'])
@app.route("/lawyer/profile/user/<int:id>", methods=['GET'])
def abogado_perfil_user(id=None):
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

@app.route("/lawyer/profile/client", methods=['GET'])
@app.route("/lawyer/profile/client/<int:id>", methods=['GET'])
def abogado_perfil_cliente(id=None):
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

@app.route("/lawyer/profile/case", methods=['GET'])
@app.route("/lawyer/profile/case/<int:id>", methods=['GET'])
def abogado_perfil_caso(id=None):
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
         
@app.route("/lawyer/profile/document", methods=['GET'])
@app.route("/lawyer/profile/document/<int:id>", methods=['GET'])
def abogado_perfil_documento(id=None):
   if request.method == "GET":
      if id is not None:
         document = Document.query.get(id)
         if document:
               return jsonify(document.serialize()), 200
         else:
               return jsonify({"msg":"document not found"}), 404
      else:
         document = Document.query.all()
         document = list(map(lambda document: document.serialize(), document))
         return jsonify(document), 200
   
@app.route("/lawyer/profile/cases/case", methods=['GET'])
@app.route("/lawyer/profile/cases/<int:id>", methods=['GET'])
def abogado_consulta_case(id=None):
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

   
@app.route("/lawyer/profile/cases/message", methods=['GET'])
@app.route("/lawyer/profile/cases/<int:id>", methods=['GET'])
def abogado_consulta_message(id=None):
#get message
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

@app.route("/lawyer/profile/query", methods=['GET', 'POST'])
@app.route("/lawyer/profile/query/<int:id>", methods=['GET'])
def abogado_caso_chat(id=None):
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
#get message
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

@app.route("/lawyer/profile/query/user", methods=['GET', 'POST'])
@app.route("/lawyer/profile/query/user/<int:id>", methods=['GET'])
def abogado_caso_user(id=None):

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