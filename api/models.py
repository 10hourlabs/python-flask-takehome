
from this import d
from unicodedata import name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    availability_status = db.Column(
        db.String(120), unique=True, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey(
        'company.id'), nullable=False)
    company = db.relationship(
        'Company', backref=db.backref('company', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.name


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(
        'User', backref=db.backref('user', lazy=True))
    client_id = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=False)
    client = db.relationship(
        'Client', backref=db.backref('client', lazy=True))

    def __repr__(self):
        return '<Schedule %r>' % self.id


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Company %r>' % self.name


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def _repr__(self):
        return '<Client %r>' % self.name


# uncomment this code and run it once after that you should comment it back
db.create_all()
