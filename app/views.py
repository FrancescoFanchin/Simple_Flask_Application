"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import AddMeasureForm,GetMeasuresForm
from app.models import Measure
from datetime import datetime
from sqlalchemy import func



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/measurements')
def show_measures():
    measures = db.session.query(Measure).all()
    """Render the website's show measures page."""
    return render_template('show_measures.html', measures=measures)

@app.route('/add-measure', methods=['POST', 'GET'])
def add_measure():
    measure_form = AddMeasureForm()

    if request.method == 'POST':
        if measure_form.validate_on_submit():
            # Get validated data from form
            id = db.session.query(func.max(Measure.id)+1)
            now=datetime.now()
            timestamp=now.strftime("%Y-%m-%d %H:%M:%S.%f") 
            temperature = measure_form.temperature.data
            duration = measure_form.duration.data
            uploaded_by="form submission"
            request_timestamp=""
            # save measure to database
            measure = Measure(id,timestamp,temperature,duration,uploaded_by,request_timestamp)
            db.session.add(measure)
            db.session.commit()

            flash('Measure successfully added')
            return redirect(url_for('show_measures'))

    flash_errors(measure_form)
    """Render the website's add measure page."""
    return render_template('add_measure.html', form=measure_form)


@app.route('/get-measures', methods=['POST', 'GET'])
def get_measures():
    measure_form = GetMeasuresForm()
	
    if request.method == 'POST':
        if measure_form.validate_on_submit():
            id_min = measure_form.id_min.data
            id_max = measure_form.id_max.data
            measures=db.session.query(Measure).filter(Measure.id.between(id_min,id_max)).all()
            for measure in measures:
                measure.request_timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            db.session.commit()
            flash("success!")
            """Render the website's get requested measures page."""
            return render_template('get_requested_measures.html',measures=measures)
            
            
    flash_errors(measure_form)
    """Render the website's get measures page."""
    return render_template('get_measures.html', form=measure_form)
        	
@app.route('/get-requested-measures', methods=['POST', 'GET'])     
def get_requested_measures(measures):
    return ""

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
