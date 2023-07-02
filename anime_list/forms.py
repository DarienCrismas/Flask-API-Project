from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Optional

class UserSignUpForm(FlaskForm):
    username = StringField("username", validators= [DataRequired()])
    first_name = StringField("first_name", validators= [DataRequired()])
    last_name = StringField("last_name", validators= [DataRequired()])
    email = StringField("email", validators= [DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    submit_button = SubmitField()

    
class UserLoginForm(FlaskForm):
    username = StringField("username", validators= [DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit_button = SubmitField()

class WatchedForm(FlaskForm):
    title = StringField("title", validators= [DataRequired()])
    synopsis = StringField("synopsis", validators=[Optional()])
    episodes = IntegerField("episodes", validators=[Optional()])
    rank = StringField("rank", validators=[Optional()])
    rating = StringField("rating", validators=[Optional()])
    aired = StringField("aired", validators=[Optional()])
    status = StringField("status", validators=[Optional()])
    score = StringField("score", validators=[Optional()])
    user_score = IntegerField("user score", validators=[Optional()])
    submit_button = SubmitField()

class UnwatchedForm(FlaskForm):
    title = StringField("title", validators= [DataRequired()])
    synopsis = StringField("synopsis", validators=[Optional()])
    episodes = IntegerField("episodes", validators=[Optional()])
    rank = StringField("rank", validators=[Optional()])
    rating = StringField("rating", validators=[Optional()])
    aired = StringField("aired", validators=[Optional()])
    status = StringField("status", validators=[Optional()])
    score = StringField("score", validators=[Optional()])
    submit_button = SubmitField()


