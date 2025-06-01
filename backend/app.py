from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from config.db import db, User, Profile, Referral
import os

try:
    import openai
except ImportError:  # pragma: no cover - openai may not be installed
    openai = None

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qplusplus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'changeme'
app.config['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY', '')
CORS(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'User exists'}), 400
    hashed = generate_password_hash(data['password'])
    user = User(email=data['email'], password=hashed)
    db.session.add(user)
    db.session.commit()
    profile = Profile(user_id=user.id)
    db.session.add(profile)
    db.session.commit()
    return jsonify({'message': 'Registered'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Logged in', 'user_id': user.id})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    profile = Profile.query.filter_by(user_id=user_id).first()
    if not profile:
        return jsonify({'message': 'Profile not found'}), 404
    return jsonify({'iq': profile.iq, 'eq': profile.eq, 'aq': profile.aq})


@app.route('/api/profile/<int:user_id>', methods=['POST'])
def update_profile(user_id):
    data = request.json
    profile = Profile.query.filter_by(user_id=user_id).first()
    if not profile:
        return jsonify({'message': 'Profile not found'}), 404
    profile.iq = data.get('iq', profile.iq)
    profile.eq = data.get('eq', profile.eq)
    profile.aq = data.get('aq', profile.aq)
    db.session.commit()
    return jsonify({'message': 'Profile updated'})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    if openai and app.config.get('OPENAI_API_KEY'):
        openai.api_key = app.config['OPENAI_API_KEY']
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": user_message}]
            )
            gpt_response = completion.choices[0].message['content']
        except Exception:
            gpt_response = "GPT service error"
    else:
        gpt_response = f"GPT-4o would respond to: {user_message}"
    return jsonify({'response': gpt_response})

@app.route('/api/referral', methods=['POST'])
def referral():
    data = request.json
    ref = Referral(referrer_email=data['referrer'], referred_email=data['referred'])
    db.session.add(ref)
    db.session.commit()
    return jsonify({'message': 'Referral recorded'})

@app.route('/api/pay', methods=['POST'])
def pay():
    data = request.json
    ref = Referral.query.filter_by(referred_email=data['email']).first()
    if ref:
        ref.paid = True
    return jsonify({'message': 'Payment processed (placeholder)'})

if __name__ == '__main__':
    app.run(debug=True)
