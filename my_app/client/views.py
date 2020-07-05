from my_app import app, db, jsonify
from flask import request
from my_app.model.models import User, Client, Lawyer, Case, Document, Message

@app.route("/client", methods=['GET', 'POST'])
@app.route("/client/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def clients(id=None):
   #get client
   if request.method == "GET":
     if id is not None:
         client = Client.query.get(id)
         if client:
               return jsonify(client.serialize()), 200
         else:
               return jsonify({"msg":"client not found"}), 404
      else:
         client = User.query.all()
         client = list(map(lambda client: client.serialize(), client))
         return jsonify(client), 200
   
   #post client
   if request.method == "POST":
      clients_username = request.json.get('clients_username', None)
      clients_email = request.json.get('clients_email', None)
      clients_password = request.json.get('clients_password', None)
      clients_phone = request.json.get('clients_phone', None)
      clients_rut = request.json.get('clients_rut', None)
      clients_address = request.json.get('clients_addres', None)
      clients_profession = request.json.get('clients_profession', None)
      clients_nationality = request.json.get('clients_nationality', None)
      clients_civil_status = request.json.get('clients_civil_status', None)
      clients_avatar = request.json.get('clients_avatar', None)

      if not clients_username:
         return jsonify({"msg":"username is required"}), 422

      if not clients_email:
         return jsonify({"msg":"email is required"}), 422

      if not clients_password:
         return jsonify({"msg":"password is required"}), 422

      if not clients_phone:
         return jsonify({"msg":"phone is required"}), 422

      if not clients_rut:
         return jsonify({"msg":"rut is required"}), 422

      if not clients_address:
         return jsonify({"msg":"address is required"}), 422
      
      if not clients_profession:
         return jsonify({"msg":"profession is required"}), 422

      if not clients_nationality:
         return jsonify({"msg":"nationality is required"}), 422

      if not clients_civil_status:
         return jsonify({"msg":"civil status is required"}), 422

      if not clients_avatar:
         return jsonify({"msg":"avatar is required"}), 422
         
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

   