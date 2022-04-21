from tokenize import Number
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError, IntegerField, FileField
from wtforms.validators import EqualTo, DataRequired, Email, Length, NumberRange, FileAllowed

def colorordbchecked(form, color, dbsided):
    if color.data != 0 and dbsided.data != 0:
        raise ValidationError("Color Prints Cannot be Double Sided.")

#User login will go here

#File, number of copies (max 5), color?, double sided?, landscape?, print all pages?
class PrintRequest(FlaskForm):
    #wtforms.widgets.FileInput
    #parameter: multiple – allow choosing multiple files
    file = FileField("File", validators=[FileAllowed(['doc','docx','gif','jpeg','jpeg','jpg','odf','odg','ods','odt','pdf','png','ppt','pptx','ps','rtf','svg','txt','xls','xlsx'])])
    #Integer Field
    copies = IntegerField("Number of Copies", validators=[NumberRange(min=1,max=5)])
    #wtforms.widgets.CheckboxInput
    color = BooleanField("Color")
    dbsided = BooleanField("Double Sided", validators=[colorordbchecked()])
    landscape = BooleanField("Landscape")
    printall = BooleanField("Print All Pages")
    print = SubmitField("Print")


