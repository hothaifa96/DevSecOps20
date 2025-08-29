from flask import Blueprint, request, jsonify
from utils.utils import users, L
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from dao.user import User
from utils.db import db

user_bp = Blueprint('user_bp', __name__)


@user_bp.post('/signup')
def signup():
    try:
        data = request.json
        if 'password' not in request.json.keys() or 'username' not in request.json.keys():
            return 'name and password are required ', 403
        data['password'] = generate_password_hash(data['password'])
        print(data)
        for user in users:
            if user['username'] == data['username']:
                return 'already exists', 403

        # users.append(data)
        user1 = User(username=data['username'], password=data['password'])
        db.session.add(user1)
        db.session.commit()
        L.log(f'user added [{data["username"]}]')
        return 'got it', 201
    except Exception as e:
        return str(e), 200


@user_bp.post('/login')
def login():
    username = request.json['username']
    password = request.json['password']

    user_data = get_user(username)
    if not user_data or not check_password_hash(user_data['password'], password):
        return {'msg': "username or password incorrect"}, 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


def get_user(username):
    return [u for u in users if u['username'] == username][0]


@user_bp.get('/')
def get_all_users():
    return users
