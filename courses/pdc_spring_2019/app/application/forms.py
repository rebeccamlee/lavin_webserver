from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField, TextAreaField, SubmitField, validators, widgets
from application.models import *
from wtforms_alchemy import ModelFieldList, model_form_factory
from wtforms.fields import FormField
from wtforms.widgets import TextArea


ModelForm = model_form_factory(Form)

class LoginForm(Form):
    username = TextField('Username', [validators.required()])
    password = PasswordField('Password', [validators.required()])

class CreateActivity(ModelForm):
    class Meta:
        model = Activity
    public =  SelectField('Privacy', choices = [(1,"Private"), (2, "Public")],  coerce=int)

class CreateAssignment(ModelForm):
    class Meta:
        model = Assignment
    public =  SelectField('Privacy', choices = [(1,"Private"), (2, "Public")], coerce=int)
class CreateReading(ModelForm):
    class Meta:
        model = Reading
    public =  SelectField('Privacy', choices = [(1,"Private"), (2, "Public")], coerce=int)

class CreateCollection(ModelForm):
    class Meta:
        model = Collection
    public =  SelectField('Privacy', choices = [(1,"Private"), (2, "Public")], coerce=int)

class CKEditor(TextArea):
    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = u'%s %s' % ('ckeditor', c)
        return super(CKEditor, self).__call__(field, **kwargs)

class CKEditorField(TextAreaField):
    widget = CKEditor()