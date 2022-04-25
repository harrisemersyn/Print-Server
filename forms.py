from tokenize import Number
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError, IntegerField
from wtforms.validators import EqualTo, DataRequired, Email, Length, NumberRange
from wtforms_validators import AlphaNumeric

#User login 
class LoginForm(FlaskForm):
    netid = StringField("NetID", validators=[DataRequired(), AlphaNumeric()])
    password = PasswordField("Password", validators=[DataRequired()])

#File, number of copies (max 5), color?, double sided?, landscape?, print all pages?
#Seperate forms for color and black and white, will pick color or black and white before going to main print form
class PrintRequestBW(FlaskForm):
    file = FileField("File", validators=[FileRequired(), FileAllowed(['doc','docx','gif','jpeg','jpeg','jpg','odf','odg','ods','odt','pdf','png','ppt','pptx','ps','rtf','svg','txt','xls','xlsx'], "Wrong Format")])
    copies = IntegerField("Number of Copies", validators=[DataRequired(), NumberRange(min=1,max=5)])
    dbsided = BooleanField("Double Sided")
    landscape = BooleanField("Landscape")
    printall = BooleanField("Print All Pages")
    print = SubmitField("Print")

class PrintRequestColor(FlaskForm):
    file = FileField("File", validators=[FileRequired(), FileAllowed(['doc','docx','gif','jpeg','jpeg','jpg','odf','odg','ods','odt','pdf','png','ppt','pptx','ps','rtf','svg','txt','xls','xlsx'], "Wrong Format")])
    copies = IntegerField("Number of Copies", validators=[DataRequired(), NumberRange(min=1,max=5)])
    landscape = BooleanField("Landscape")
    printall = BooleanField("Print All Pages")
    print = SubmitField("Print")


