from my_app import app, db, jsonify
from flask import request
from my_app.model.models import User, Client, Lawyer, Case, Document, Message

@app.route("/case", methods=['GET', 'POST'])
@app.route("/case/<int:cases_id>", methods=['GET', 'PUT', 'DELETE'])
def cases(cases_id=None):
  #get cases
  if request.method == "GET":
     if cases_id is not None:
        case = Case.query.filter( Case.cases_id == cases_id).first()
        if case:
              return jsonify(case.serialize()), 200
        else:
              return jsonify({"msg":"case not found"}), 404
     else:
        case = Case.query.all()
        case = list(map(lambda case: case.serialize(), case))
        return jsonify(case), 200

  #post cases
  if request.method == "POST":
    cases_matter = request.json.get('cases_matter', None)
    cases_date = request.json.get('cases_date', None)
    cases_description = request.json.get('cases_description', None)

    if not cases_matter:
      return jsonify({"msg":"matter is required"}), 422

    if not cases_date:
      return jsonify({"msg":"date is required"}), 422

    if not cases_description:
      return jsonify({"msg":"description is required"}), 422
        
    case = Case()
    case.cases_matter = cases_matter
    case.cases_date = cases_date
    case.cases_description = cases_description

    db.session.add(case)
    db.session.commit()

    return jsonify(case.serialize()), 201

    if cases_id is not None:
      user = User.query.filter_by(id).delete()

    db.session.delete(user)
    db.session.commit()

  #put cases
  if request.method == "PUT":
    incomingData = request.get_json()
    updateData = Case.query.filter_by(cases_id=cases_id)

    listOfNotEmptyStrings = []
    for item in incomingData:
      if incomingData[item] != "":
          listOfNotEmptyStrings.append(item)

    for item2 in listOfNotEmptyStrings:
          print(incomingData[item2], item2)
          updateData.update({item2: incomingData[item2]})
          db.session.commit()
    return "Case is updated"

  #delete cases
  if request.method == "DELETE":

     case = Case.query.filter( Case.cases_id == cases_id).first()
      
  if not case:
    return jsonify({"msg":"Case not found"}), 404

  db.session.delete(case)
  db.session.commit()

  return jsonify({"msg": "Case deleted"}), 200