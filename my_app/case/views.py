from my_app import app, db, jsonify
from flask import request
from my_app.model.models import User, Client, Lawyer, Case, Document, Message

@app.route("/case", methods=['GET', 'POST'])
@app.route("/case/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def cases(id=None):
  #get cases
  if request.method == "GET":
    if id is not None:
        case = Case.query.get(id)
        if cases:
              return jsonify(cases.serialize()), 200
        else:
              return jsonify({"msg":"cases not found"}), 404
     else:
        cases = Case.query.all()
        cases = list(map(lambda cases: cases.serialize(), cases))
        return jsonify(cases), 200
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