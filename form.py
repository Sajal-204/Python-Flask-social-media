from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField ,PasswordField ,BooleanField
from wtforms.validators import DataRequired ,Length , Email , EqualTo

class Sign_up(FlaskForm):
    username=StringField("username",validators=[DataRequired() , Length(min=2,max=20)])
    email=StringField("Email" , validators=[DataRequired() , Email()])
    password=PasswordField("enter password", validators=[DataRequired()])
    confirm_password=PasswordField("confirm password", validators=[DataRequired(), EqualTo("password")])
    submit=SubmitField("Sign up")
    
class Login(FlaskForm):
    email=StringField("Email" , validators=[DataRequired() , Email()])
    password=PasswordField("enter password", validators=[DataRequired()])
    remember_me=BooleanField("Remember Me")
    submit=SubmitField("Login")