import datetime

from flask import Flask, request, g, jsonify
from routes.movies import movie_bp
from routes.users import user_bp
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity
from utils.utils import L
from utils.db import db  # Import from the new file

app = Flask('movies-api')
app.config['JWT_SECRET_KEY'] = 'my secret string'
jwt = JWTManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db.init_app(app)


@app.before_request
def before_rq():
    L.log(f'{request.host} {request.date} -> {request.base_url}')
    g.start_time = datetime.datetime.now()


@app.after_request
def after_rg(response):
    end_time = datetime.datetime.now()
    duration = end_time - g.start_time
    L.log(f'duration [{duration.total_seconds()}] ')
    return response


app.register_blueprint(movie_bp, url_prefix='/movies')
app.register_blueprint(user_bp, url_prefix='/user')


@app.route('/')
def homepage():
    return 'hello'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5001)
