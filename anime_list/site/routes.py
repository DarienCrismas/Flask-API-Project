from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from anime_list.forms import WatchedForm, UnwatchedForm
from anime_list.models import db, Watched, Unwatched
from anime_list.api_func import get_id, get_synopsis, get_episodes, get_rank, get_rating, get_airdates, get_status, get_score


site = Blueprint("site", __name__, template_folder = "site_templates")

@site.route("/")
def home():
    print("end my suffering")
    return render_template("index.html")

@site.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


#WATCHED
@site.route("/watched", methods=["GET", "POST"])
@login_required
def watched():
    watchedform = WatchedForm()
    try:
        if request.method == "POST" and watchedform.validate_on_submit():
            title = watchedform.title.data
            series_id = get_id(title)
            if watchedform.synopsis.data:
                synopsis = watchedform.synopsis.data
            else:
                synopsis = get_synopsis(series_id)
            if watchedform.episodes.data:
                episodes = watchedform.episodes.data
            else:
                episodes = get_episodes(series_id)
            if watchedform.rank.data:
                rank = watchedform.rank.data
            else:
                rank = get_rank(series_id)
            if watchedform.rating.data:
                rating = watchedform.rating.data
            else:
                rating = get_rating(series_id)
            if watchedform.aired.data:
                aired = watchedform.aired.data
            else:
                aired = get_airdates(series_id)
            if watchedform.status.data:
                status = watchedform.status.data
            else:
                status = get_status(series_id)
            if watchedform.score.data:
                score = watchedform.score.data
            else:
                score = get_score(series_id)
            user_score = watchedform.user_score.data
            user_token = current_user.token

            watched = Watched(title, synopsis, episodes, rank, rating, aired, status, score, user_score, user_token)
            
            db.session.add(watched)
            db.session.commit()

            return redirect(url_for("site.watched"))
    except:
        raise Exception("Series not added, please check your form and try again.")

    user_token = current_user.token
    watched = Watched.query.filter_by(user_token=user_token)
    return render_template("watched.html", form=watchedform, watched = watched)

@site.route("/watched/<id>")
@login_required
def remove_watched(id):
    series = Watched.query.get(id)
    db.session.delete(series)
    db.session.commit()
    print("should be deleted")
    return redirect(url_for("site.watched"))



#UNWATCHED
@site.route("/unwatched", methods=["GET", "POST"])
@login_required
def unwatched():
    unwatchedform = UnwatchedForm()
    try:
        if request.method == "POST" and unwatchedform.validate_on_submit():
            title = unwatchedform.title.data
            series_id = get_id(title)
            if unwatchedform.synopsis.data:
                synopsis = unwatchedform.synopsis.data
            else:
                synopsis = get_synopsis(series_id)
            if unwatchedform.episodes.data:
                episodes = unwatchedform.episodes.data
            else:
                episodes = get_episodes(series_id)
            if unwatchedform.rank.data:
                rank = unwatchedform.rank.data
            else:
                rank = get_rank(series_id)
            if unwatchedform.rating.data:
                rating = unwatchedform.rating.data
            else:
                rating = get_rating(series_id)
            if unwatchedform.aired.data:
                aired = unwatchedform.aired.data
            else:
                aired = get_airdates(series_id)
            if unwatchedform.status.data:
                status = unwatchedform.status.data
            else:
                status = get_status(series_id)
            if unwatchedform.score.data:
                score = unwatchedform.score.data
            else:
                score = get_score(series_id)
            user_token = current_user.token

            unwatched = Unwatched(title, synopsis, episodes, rank, rating, aired, status, score, user_token)
            
            db.session.add(unwatched)
            db.session.commit()

            return redirect(url_for("site.unwatched"))
    except:
        raise Exception("Series not added, please check your form and try again.")

    user_token = current_user.token
    unwatched = Unwatched.query.filter_by(user_token=user_token)
    return render_template("unwatched.html", form=unwatchedform, unwatched = unwatched)



@site.route("/unwatched/<id>")
@login_required
def remove_unwatched(id):
    series = Unwatched.query.get(id)
    db.session.delete(series)
    db.session.commit()
    print("should be deleted")
    return redirect(url_for("site.unwatched"))
