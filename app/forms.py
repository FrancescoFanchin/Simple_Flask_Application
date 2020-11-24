from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class AddMeasureForm(FlaskForm):
    #only temperature and duration fields are supposed to be inserted manually
    temperature = StringField('temperature', validators=[InputRequired()])
    duration = StringField('duration', validators=[InputRequired()])
    
class GetMeasuresForm(FlaskForm):
    #get measure by id range
	id_min = StringField('id_min', validators=[InputRequired()])
	id_max = StringField('id_max', validators=[InputRequired()])

