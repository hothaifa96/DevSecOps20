from flask import Blueprint, jsonify, request
from utils.utils import movies, L
from flask_jwt_extended import jwt_required, get_jwt_identity

movie_bp = Blueprint('movie_bp', __name__)


@movie_bp.get('/')
def get_all():
    return jsonify(movies)


@movie_bp.get('/<int:id>')
@jwt_required()
def get_by_id(id):
    for movie in movies:
        if movie.get('id') == id:
            print(get_jwt_identity())
            return jsonify(movie)
    return jsonify({'status': 'not found'}), 404


@movie_bp.post('/')
@jwt_required()
def add_movie():
    new_movie = request.json
    if not new_movie or 'name' not in new_movie:
        return jsonify({'status': 'bad request', 'message': 'name is required'}), 400

    new_id = max([movie['id'] for movie in movies], default=0) + 1
    new_movie['id'] = new_id
    movies.append(new_movie)
    L.log(f'Movie added {new_movie["name"]}')
    return jsonify(new_movie), 201


@movie_bp.put('/<int:id>')
def update_movie(id):
    update_data = request.json

    if not update_data:
        return jsonify({'status': 'bad request', 'message': 'no data provided'}), 400

    for movie in movies:
        if movie.get('id') == id:
            if 'name' in update_data:
                movie['name'] = update_data['name']
            if 'rate' in update_data:
                movie['rate'] = update_data['rate']
            return jsonify(movie)

    return jsonify({'status': 'not found'}), 404


@movie_bp.delete('/<int:id>')
def delete_by_id(id):
    for i, movie in enumerate(movies):
        if movie.get('id') == id:
            deleted_movie = movies.pop(i)
            return jsonify({'status': 'deleted', 'movie': deleted_movie})

    return jsonify({'status': 'not found'}), 404


@movie_bp.delete('/')
def delete_all():
    deleted_count = len(movies)
    movies.clear()
    return jsonify({'status': 'deleted', 'count': deleted_count})
