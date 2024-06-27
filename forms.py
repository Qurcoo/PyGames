from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, DateField, RadioField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, equal_to
from flask_wtf.file import FileField, FileRequired

class PostForm(FlaskForm):
    File_inp = FileField("ატვირთეთ ფაილი", validators=[DataRequired()])
    abtGame = StringField("მოგვიყევით თქვენი თამაშის შესახებ", validators=[DataRequired(), Length(min=1, max=100)])
    email = EmailField("შეიყვანეთ მეილი", validators=[DataRequired()])
    Post = SubmitField("ატვირთვა")

class EditUserForm(FlaskForm):
    username = StringField("მომხმარებლის სახელი")
    email = EmailField("თქვენი მეილი")
    abtGame = StringField("ინფორმაცია...")
    File_inp = FileField("მიუთითეთ ფაილი", validators=[DataRequired()])
    save = SubmitField("ცვლილებების შენახვა")

class RegisterForm(FlaskForm):
    username = StringField("მომხმარებლის სახელი", validators=[DataRequired(), Length(min=1, max=12)])
    password = PasswordField("თქვენი პაროლი", validators=[DataRequired(), Length(min=8, max=20)])
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(), equal_to("password", message="გაიმეორეთ პაროლი")])
    register = SubmitField("რეგისტრაცია")

class LoginForm(FlaskForm):
    username = StringField("შეიყვანეთ თქვენი სახელი")
    password = PasswordField("შეიყვანეთ თქვენი პაროლი")

    login = SubmitField("ავტორიზაცია")
