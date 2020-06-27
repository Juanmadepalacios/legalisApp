from my_app import db
from sqlalchemy.sql import func
import datetime


class Client(db.Model):
    __tablename__='clients'
    clients_id = db.Column(db.Integer, primary_key=True)
    clients_username = db.Column(db.String(30), unique=True, nullable=False)
    clients_email = db.Column(db.String(100), unique=True, nullable=True)
    clients_password = db.Column(db.String(100), unique=False, nullable=False)
    clients_phone = db.Column(db.Integer, unique=True, nullable=True)
    clients_rut = db.Column(db.String(30), unique=True, nullable=True)
    clients_address = db.Column(db.String(80), unique=False, nullable=True)
    clients_profession = db.Column(db.String(30), unique=False, nullable=True)
    clients_nationality = db.Column(db.String(30), unique=False, nullable=True)
    clients_civil_status = db.Column(db.String(20), unique=False, nullable=True)
    clients_avatar = db.Column(db.Integer, unique=False, nullable=True, default=1)
    cases = db.relationship('Case', backref='client')
    
    
    
    def __repr__(self):
        return '<Client %r>' % self.clients_id, self.clients_username, self.clients_email, self.clients_password, self.clients_phone, self.clients_rut, self.clients_address, self.clients_profession, self.clients_nationality, self.clients_civil_status, self.clients_avatar

    def serialize(self):
        return {
            "clients_id": self.clients_id,
            "clients_username": self.clients_username,
            "clients_email": self.clients_email,
            "clients_password": self.clients_password,
            "clients_phone": self.clients_phone,
            "clients_rut": self.clients_rut,
            "clients_address": self.clients_address,
            "clients_profession": self.clients_profession,
            "clients_nationality": self.clients_nationality,
            "clients_civil_status": self.clients_civil_status,
            "clients_avatar": self.clients_avatar
        }

   

class User(db.Model):
    __tablename__='users'
    users_id = db.Column(db.Integer, primary_key=True)
    users_name = db.Column(db.String(30), unique=False, nullable=False)
    users_issue_subject = db.Column(db.String(30), unique=False, nullable=False)
    users_issue_description = db.Column(db.Text(3000), unique=False, nullable =False)
    messages = db.relationship('Message', backref='users') 
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyers.lawyers_id'))
    

    def __repr__(self):
        return '<User %r>' % self.users_id, self.users_name, self.users_issue_subject, self.users_issue_description
    
    def serialize(self):
        return {
            "users_id": self.users_id,
            "users_name": self.users_name,
            "users_issue_subject": self.users_issue_subject,
            "users_issue_description": self.users_issue_description
        }

class Rol(db.Model):
    __tablename__='rols'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=False, nullable = False)
    code = db.Column(db.String(20), unique=True, nullable = False )

    def __repr__(self):
        return '<Rol %r>' % self.name, self.code

    def serialize(self):
        return {
            "name": self.name,
            "code": self.code
        }


class Lawyer(db.Model):
    __tablename__='lawyers'
    lawyers_id = db.Column(db.Integer, primary_key=True)
    lawyers_name = db.Column(db.String(30), unique=True, nullable=False)
    lawyers_password = db.Column(db.String(30), unique=False, nullable=False)
    lawyers_email = db.Column(db.String(100), unique=True, nullable=True)
    lawyers_rut = db.Column(db.String(30), unique=True, nullable=False)
    lawyers_phone = db.Column(db.Integer, unique=True, nullable= True)
    lawyers_field = db.Column(db.String(15), unique=True, nullable=False)
    lawyers_title = db.Column(db.Integer, unique=False, nullable=False)
    lawyers_file_speciality = db.Column(db.Integer, unique=False, nullable=True )
    lawyers_bank = db.Column(db.String(30), unique=False, nullable=False)
    lawyers_account = db.Column(db.String(15), unique=False, nullable=False)
    lawyers_bank_number = db.Column(db.Integer, unique=True, nullable=False)
    lawyers = db.relationship('User', backref='lawyers')
    
    #tipo de cuenta
    #Banco
    #numero de cuenta
    def __repr__(self):
        return '<Lawyer %r>' % self.lawyers_id, self.lawyers_name, self.lawyers_password, self.lawyers_email, self.lawyers_rut, self.lawyers_phone, self.lawyers_field, self.lawyers_title, self.lawyers_file_speciality, self.lawyers_bank, self.lawyers_account, self.lawyers_bank_number
    
    def serialize(self):
        return {
            "lawyers_id": self.lawyers_id,
            "lawyers_name": self.lawyers_name,
            "lawyers_password": self.lawyers_password,
            "lawyers_email": self.lawyers_email,
            "lawyers_rut": self.lawyers_rut,
            "lawyers_phone": self.lawyers_phone,
            "lawyers_field": self.lawyers_field,
            "lawyers_title": self.lawyers_title,
            "lawyers_file_speciality": self.lawyers_file_speciality, 
            "lawyers_bank": self.lawyers_bank,
            "lawyers_account": self.lawyers_account,
            "lawyers_bank_number": self.lawyers_bank_number
        }
    
lawyer_case = db.Table('lawyer_case',

    db.Column('lawyers_id', db.Integer, db.ForeignKey('lawyers.lawyers_id'), primary_key=True),
    db.Column('cases_id', db.Integer, db.ForeignKey('cases.cases_id'), primary_key=True)
)

class Case(db.Model):
    __tablename__ ='cases'
    cases_id = db.Column(db.Integer, primary_key=True)
    cases_matter = db.Column(db.String(20), unique=False, nullable=False)
    cases_date = db.Column(db.DateTime, unique=False, nullable=False)
    cases_description = db.Column(db.Text(300), unique=False, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.clients_id'))
    cases_documents = db.relationship('Document', backref='Case', lazy=True)
    lawyers_case = db.relationship('Lawyer', secondary=lawyer_case, lazy='subquery', backref=db.backref('case', lazy=True))

    def __repr__(self):
       return '<Case %r>' % self.cases_id, self.cases_matter, self.cases_date, self.cases_description 

    def serialize(self):
        return {
            "cases_id": self.cases_id,
            "cases_matter": self.cases_matter,
            "cases_date": self.cases_date,
            "cases_description": self.cases_description
        }


class Document(db.Model):
    __tablename__='documents'
    documents_id = db.Column(db.Integer, primary_key=True) 
    documents_files = db.Column(db.Integer, unique=False, nullable=True)
    case_id = db.Column(db.Integer, db.ForeignKey('cases.cases_id'), nullable=False)

    def __repr__(self):
        return '<Document %r>' % self.documents_id, self.documents_files
    
    def serialize(self):
        return {
            "documents_id": self.documents_id,
            "documents_file": self.documents_files
        }


class Message(db.Model):
    __tablename__='messages'
    messages_id = db.Column(db.Integer, primary_key=True)
    messages_date = db.Column(db.DateTime, unique=False, nullable = False, server_default=func.now())
    messages_content = db.Column(db.Text(20000), unique=False, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.users_id'))
    

    def __repr__(self):
        return '<Message %r>' % self.messages_id, self.messages_date, messages_content
    
    def serialize(self):
        return {
            "messages_id": self.messages_id,
            "messages_date": self.messages_date,
            "messages_content": self.messages_content
        }





#class payment
# relationship client
