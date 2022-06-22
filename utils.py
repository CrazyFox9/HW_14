import sqlite3
from collections import Counter


class DbConnect:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()


def movie_by_title(title):
    db_connect = DbConnect('netflix.db')
    query = f"""
            SELECT title, country, release_year, listed_in, description
            from netflix
            where title like '%{title}%'
            order by release_year desc
            limit 1
    """
    db_connect.cur.execute(query)

    result = db_connect.cur.fetchone()
    return {
        "title": result[0],
        "country": result[1],
        "release_year": result[2],
        "genre": result[3],
        "description": result[4]
    }


def movies_by_years(year_1, year_2):
    db_connect = DbConnect('netflix.db')
    query = f"""
            SELECT title, release_year from netflix
            where release_year between {year_1} and {year_2}
            order by release_year
            limit 100
    """

    db_connect.cur.execute(query)
    result = db_connect.cur.fetchall()
    movies = []
    for movie in result:
        movies.append({"title": movie[0],
                       "release_year": movie[1]})
    return movies


def movies_by_rating(rating):
    db_connect = DbConnect('netflix.db')
    rating_parameters = {
        "children": "'G'",
        "family": "'G', 'PG', 'PG-13'",
        "adult": "'R', 'NC-17'"
    }
    query = f"""
            SELECT title, rating, description from netflix
            where rating in ({rating_parameters[rating]})
    """

    db_connect.cur.execute(query)

    result = db_connect.cur.fetchall()
    movies = []

    for movie in result:
        movies.append({
            "title": movie[0],
            "rating": movie[1],
            "description": movie[2]
        })

    return movies


def movies_by_genre(genre):
    db_connect = DbConnect('netflix.db')
    query = f"""
            SELECT title, description from netflix
            where listed_in like'%{genre}%'
            order by release_year desc
            limit 10
    """

    db_connect.cur.execute(query)

    result = db_connect.cur.fetchall()
    movies = []

    for movie in result:
        movies.append({
            "title": movie[0],
            "description": movie[1]
        })

    return movies


def cast_partners(actor_1, actor_2):
    db_connect = DbConnect('netflix.db')
    query = f"""
            SELECT `cast` from netflix
            where `cast` like '%{actor_1}%' and `cast` like '%{actor_2}%'
    """
    db_connect.cur.execute(query)

    result = db_connect.cur.fetchall()
    actors_list = []

    for cast in result:
        actors_list.extend(cast[0].split(', '))

    counter = Counter(actors_list)
    result_list = []

    for actor, count in counter.items():
        if actor not in [actor_1, actor_2] and count > 2:
            result_list.append(actor)

    return result_list


def movies_by_parameters(movie_type, release_year, genre):
    db_connect = DbConnect('netflix.db')
    query = f"""
            SELECT title, description from netflix
            where type = '{movie_type}'
            and release_year = '{release_year}'
            and listed_in like '%{genre}%'
    """

    db_connect.cur.execute(query)

    result = db_connect.cur.fetchall()
    result_list = []

    for movie in result:
        result_list.append({
            "title": movie[0],
            "description": movie[1]
        })

    return result_list
