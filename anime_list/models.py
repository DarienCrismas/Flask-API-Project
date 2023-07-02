from flask_sqlalchemy import SQLAlchemy
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash
import secrets
from flask_login import UserMixin, LoginManager
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    username = db.Column(db.String, nullable = False)
    first_name = db.Column(db.String(150), nullable = True, default = "")
    last_name = db.Column(db.String(150), nullable = True, default = "")    
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = False, default = "")
    token = db.Column(db.String, default = "", unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    watched = db.relationship("Watched", backref = "owner", lazy = True)
    unwatched = db.relationship("Unwatched", backref = "owner", lazy = True)


    def __init__(self, username, first_name, last_name, email, password,):
        self.id = self.set_id()
        self.username = username 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.set_password(password)
        self.token = self.set_token()
        

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        return generate_password_hash(password)
    
    def set_token(self):
        return secrets.token_hex(24)
    
    def __repr__(self):
        return f"{self.username} has been created."
    
    
class Watched(db.Model):
    id = db.Column(db.String, primary_key = True)
    title = db.Column(db.String(50))
    synopsis = db.Column(db.Text, nullable = True)
    episodes = db.Column(db.String(5), nullable = True)
    rank = db.Column(db.String(50), nullable = True)
    rating = db.Column(db.String(70), nullable = True)
    aired = db.Column(db.String(50), nullable = True)
    status = db.Column(db.String(50), nullable = True)
    score = db.Column(db.String(50), nullable = True)
    user_score = db.Column(db.String(5), nullable = True)
    user_token = db.Column(db.String, db.ForeignKey("user.token"), nullable = False)


    def __init__(self, title, synopsis, episodes, rank, rating, aired, status, score, user_score, user_token):
        self.id = self.set_id()
        self.title = title
        self.synopsis = synopsis
        self.episodes = episodes
        self.rank = rank
        self.rating = rating
        self.aired = aired
        self.status = status
        self.score = score    
        self.user_score = user_score 
        self.user_token = user_token

    def set_id(self):
        return str(uuid.uuid4())
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f"{self.series} has been added to the database."
    
class Unwatched(db.Model):
    id = db.Column(db.String, primary_key = True)
    title = db.Column(db.String(50))
    synopsis = db.Column(db.Text, nullable = True)
    episodes = db.Column(db.String(5), nullable = True)
    rank = db.Column(db.String(50), nullable = True)
    rating = db.Column(db.String(70), nullable = True)
    aired = db.Column(db.String(50), nullable = True)
    status = db.Column(db.String(50), nullable = True)
    score = db.Column(db.String(50), nullable = True)
    user_token = db.Column(db.String, db.ForeignKey("user.token"), nullable = False)


    def __init__(self, title, synopsis, episodes, rank, rating, aired, status, score, user_token):
        self.id = self.set_id()
        self.title = title
        self.synopsis = synopsis
        self.episodes = episodes
        self.rank = rank
        self.rating = rating
        self.aired = aired
        self.status = status
        self.score = score    
        self.user_token = user_token

    def set_id(self):
        return str(uuid.uuid4())
    
    def __repr__(self):
        return f"{self.series} has been added to the database."
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class WatchedSchema(ma.Schema):
    class Meta:
        fields = ["id", "title", "synopsis", "episodes", "rank", "rating", "aired", "status", "score", "user_score"]

watched_schema = WatchedSchema()
watched_list_schema = WatchedSchema(many=True)

class UnwatchedSchema(ma.Schema):
    class Meta:
        fields = ["id", "title", "synopsis", "episodes", "rank", "rating", "aired", "status", "score"]

unwatched_schema = UnwatchedSchema()
unwatched_list_schema = UnwatchedSchema(many=True)
