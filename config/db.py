from flask_sqlalchemy import SQLAlchemy

# Database instance

db = SQLAlchemy()

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    referrals = db.relationship('Referral', backref='user', lazy=True)
    profile = db.relationship('Profile', backref='user', uselist=False)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    iq = db.Column(db.Integer, default=0)
    eq = db.Column(db.Integer, default=0)
    aq = db.Column(db.Integer, default=0)

class QPlusPlusScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score_type = db.Column(db.String(10))
    value = db.Column(db.Integer)

class Referral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referrer_email = db.Column(db.String(120))
    referred_email = db.Column(db.String(120))
    paid = db.Column(db.Boolean, default=False)
