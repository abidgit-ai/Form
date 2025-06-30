from datetime import datetime
from .database import db
from sqlalchemy.dialects.postgresql import JSONB

class Form(db.Model):
    __tablename__ = 'forms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    fields = db.Column(JSONB, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    submissions = db.relationship('Submission', back_populates='form', cascade='all, delete-orphan')

class Submission(db.Model):
    __tablename__ = 'submissions'
    id = db.Column(db.Integer, primary_key=True)
    form_id = db.Column(db.Integer, db.ForeignKey('forms.id'))
    data = db.Column(JSONB, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('submissions.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    form = db.relationship('Form', back_populates='submissions')
    parent = db.relationship('Submission', remote_side=[id], backref='children')
