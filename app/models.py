from app import db

class Measure(db.Model):
    __tablename__ = 'measures_table'
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.String(255))
    temperature = db.Column(db.String(255))
    duration= db.Column(db.String(255))
    uploaded_by=db.Column(db.String(255))
    request_timestamp=db.Column(db.String(255))

    def __init__(self, id,timestamp,temperature,duration,uploaded_by,request_timestamp):
        self.id = id
        self.timestamp = timestamp
        self.temperature = temperature
        self.duration = duration
        self.uploaded_by=uploaded_by
        self.request_timestamp=request_timestamp

    def __repr__(self):
        return '<Measure %r>' % self.id
