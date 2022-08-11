
from sqlalchemy_utils import ChoiceType
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

TYPES = [
    ('available', 'Available'),
    ('not available', 'Not available')
]


########### MODELS #############
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    availability_status = db.Column(
        ChoiceType(TYPES), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey(
        'company.id'), nullable=False)
    company = db.relationship(
        'Company', backref=db.backref('company', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.name


class Schedule(db.Model):
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(
        'User', backref=db.backref('user', lazy=True))
    client_id = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=False)
    client = db.relationship(
        'Client', backref=db.backref('client', lazy=True))
    date_range = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Schedule %r>' % self.id


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Schedule %r>' % self.id


class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)

    def _repr__(self):
        return '<Client %r>' % self.name


########### ROUTES #############
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/companies')
class Company(Resource):
    def get(self):
        return Company.query.all()


@api.route('/users/<int:company_id>')
class User(Resource):
    def get(self, company_id):
        return User.query.filter_by(company_id).all()
