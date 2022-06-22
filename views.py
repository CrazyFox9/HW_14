from flask import Blueprint, jsonify
from utils import *

movies_blueprint = Blueprint("movies_blueprint", __name__)


@movies_blueprint.route('/movie/<title>')
def get_by_movie_title(title):

    return movie_by_title(title)


@movies_blueprint.route('/movie/<int:year_1>/to/<int:year_2>')
def get_by_year_to_year(year_1, year_2):

    return jsonify(movies_by_years(year_1, year_2))


@movies_blueprint.route('/rating/<rating>')
def get_by_rating(rating):

    return jsonify(movies_by_rating(rating))


@movies_blueprint.route('/genre/<genre>')
def get_by_genre(genre):

    return jsonify(movies_by_genre(genre))
