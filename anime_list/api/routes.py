from flask import Blueprint, request, jsonify
from anime_list.misc_func import token_required
from anime_list.api_func import get_id, get_synopsis, get_episodes, get_rank, get_rating, get_airdates, get_status, get_score
from anime_list.models import db, Watched, watched_list_schema, watched_schema, Unwatched, unwatched_schema, unwatched_list_schema

api = Blueprint('api', __name__, url_prefix="/api")

@api.route("/getdata")
def getdata():
    return {"some": "value"}

#WATCHED SERIES
@api.route("/watched", methods = ["POST"])
@token_required
def add_watched(our_user):
    title = request.json["title"].title()
    anime_id = get_id(title)
    synopsis = get_synopsis(anime_id)
    episodes = get_episodes(anime_id)
    rank = get_rank(anime_id)
    rating = get_rating(anime_id)
    aired = get_airdates(anime_id)
    status = get_status(anime_id)
    score = get_score(anime_id)
    user_score = request.json["user_score"]
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    series = Watched(title, synopsis, episodes, rank, rating, aired, 
                  status, score, user_score, user_token)

    db.session.add(series)
    db.session.commit()

    response = watched_schema.dump(series)
    return jsonify(response)


@api.route("/watched/<id>", methods = ["GET"])
@token_required
def get_watched(id):
    if id:
        series = Watched.query.get(id)
        response = watched_schema.dump(series)
        return jsonify(response)
    else:
        return jsonify("message:", "ID is missing"), 401
    

@api.route("/watched", methods=["GET"])
@token_required
def get_watched_list(our_user):
    token = our_user.token
    series = Watched.query.filter_by(user_token = token).all()
    response = watched_list_schema.dump(series)

    return jsonify(response)



@api.route("/watched/<id>", methods = ["PUT"])
@token_required
def update_watched(our_user, id):
    series = Watched.query.get(id)

    series.title = request.json["title"].title()
    series.anime_id = get_id(series.title)
    series.synopsis = get_synopsis(series.anime_id)
    series.episodes = get_episodes(series.anime_id)
    series.rank = get_rank(series.anime_id)
    series.rating = get_rating(series.anime_id)
    series.aired = get_airdates(series.anime_id)
    series.status = get_status(series.anime_id)
    series.score = get_score(series.anime_id)
    series.user_score = request.json["user_score"]
    series.user_token = our_user.token

    db.session.commit()

    response = watched_schema.dump(series)
    return jsonify(response)


@api.route("/watched/<id>", methods = ["DELETE"])
@token_required
def remove_watched(our_user, id):
    series = Watched.query.get(id)
    db.session.delete(series)
    db.session.commit()

    response = watched_schema.dump(series)
    return jsonify(response)



#UNWATCHED SERIES
@api.route("/unwatched", methods = ["POST"])
@token_required
def add_unwatched(our_user):
    title = request.json["title"].title()
    anime_id = get_id(title)
    synopsis = get_synopsis(anime_id)
    episodes = get_episodes(anime_id)
    rank = get_rank(anime_id)
    rating = get_rating(anime_id)
    aired = get_airdates(anime_id)
    status = get_status(anime_id)
    score = get_score(anime_id)
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    series = Unwatched(title, synopsis, episodes, rank, rating, aired, 
                  status, score, user_token)

    db.session.add(series)
    db.session.commit()

    response = unwatched_schema.dump(series)
    return jsonify(response)


@api.route("/unwatched/<id>", methods = ["GET"])
@token_required
def get_unwatched(id):
    if id:
        series = Unwatched.query.get(id)
        response = unwatched_schema.dump(series)
        return jsonify(response)
    else:
        return jsonify("message:", "ID is missing"), 401
    

@api.route("/unwatched", methods=["GET"])
@token_required
def get_unwatched_list(our_user):
    token = our_user.token
    series = Unwatched.query.filter_by(user_token = token).all()
    response = unwatched_list_schema.dump(series)

    return jsonify(response)


@api.route("/unwatched/<id>", methods = ["PUT"])
@token_required
def update_unwatched(our_user, id):
    series = Unwatched.query.get(id)

    series.title = request.json["title"].title()
    series.anime_id = get_id(series.title)
    series.synopsis = get_synopsis(series.anime_id)
    series.episodes = get_episodes(series.anime_id)
    series.rank = get_rank(series.anime_id)
    series.rating = get_rating(series.anime_id)
    series.aired = get_airdates(series.anime_id)
    series.status = get_status(series.anime_id)
    series.score = get_score(series.anime_id)
    series.user_token = our_user.token

    db.session.commit()

    response = unwatched_schema.dump(series)
    return jsonify(response)


@api.route("/unwatched/<id>", methods = ["DELETE"])
@token_required
def remove_unwatched(our_user, id):
    series = Unwatched.query.get(id)
    db.session.delete(series)
    db.session.commit()

    response = unwatched_schema.dump(series)
    return jsonify(response)
