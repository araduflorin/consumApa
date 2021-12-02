from consumApa import db
from datetime import datetime
from utcnow import utcnow



class ApaRece(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    indexBuc = db.Column(db.Integer(),nullable=False)
    indexBaie = db.Column(db.Integer(),nullable=False)
    indexWCServiciu = db.Column(db.Integer(),nullable=False)
    dataConsum = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return 'Consum apa' + str(self.id)
