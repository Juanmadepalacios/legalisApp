from my_app import app, db, jsonify
from flask import request
from my_app.model.models import User, Client, Lawyer, Case, Document, Message

#vistas abogado
@app.route("/lawyer", methods=['GET', 'POST'])
@app.route("/lawyer/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def lawyers(id=None):
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
      
      db.session.add(lawyer)
      db.session.commit()

      return jsonify(lawyer.serialize()), 201

#put lawyer
   if request.method == "PUT":
      lawyers_name = request.json.get('name', None)
      lawyers_password = request.json.get('password', None)
      lawyers_email = request.json.get('email', None)
      lawyers_rut = request.json.get('rut', None)
      lawyers_phone = request.json.get('phone', None)
      lawyers_field = request.json.get('field', None)
      lawyers_title = request.json.get('title', None)
      lawyers_file_speciality = request.json.get('file speciality', None)
      lawyers_bank = request.json.get('bank', None)
      lawyers_account = request.json.get('account', None)
      lawyers_bank_number = request.json.get('bank number', None)

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

      lawyer = Lawyer.query.get(id)

      if lawyer:

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

      db.session.commit()

      return jsonify(lawyer.serialize()), 200
         
#delete lawyer
   if request.method == "DELETE":

      lawyer = Lawyer.quert.get(id)

      if not lawyer:
         return jsonify({"msg":"Lawyer not found"}), 404

      db.session.delete(lawyer)
      db.session.commit()

      return jsonify({"msg": "Lawyer deleted"}), 200