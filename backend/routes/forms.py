from flask import Blueprint, request, jsonify, send_file
from io import StringIO
import csv

from ..database import db
from ..models import Form, Submission

bp = Blueprint('forms', __name__)

@bp.route('/forms', methods=['POST'])
def create_form():
    data = request.get_json()
    form = Form(name=data['name'], fields=data.get('fields', []))
    db.session.add(form)
    db.session.commit()
    return jsonify({'id': form.id, 'name': form.name}), 201

@bp.route('/forms/<int:form_id>', methods=['GET'])
def get_form(form_id):
    form = Form.query.get_or_404(form_id)
    return jsonify({'id': form.id, 'name': form.name, 'fields': form.fields})

@bp.route('/forms', methods=['GET'])
def list_forms():
    forms = Form.query.all()
    return jsonify([
        {'id': f.id, 'name': f.name} for f in forms
    ])

@bp.route('/forms/<int:form_id>/submit', methods=['POST'])
def submit_form(form_id):
    form = Form.query.get_or_404(form_id)
    data = request.get_json()
    submission = Submission(form=form, data=data.get('data', {}), parent_id=data.get('parent_id'))
    db.session.add(submission)
    db.session.commit()
    return jsonify({'id': submission.id}), 201

@bp.route('/forms/<int:form_id>/submissions', methods=['GET'])
def list_submissions(form_id):
    form = Form.query.get_or_404(form_id)
    results = [
        {'id': s.id, 'data': s.data, 'parent_id': s.parent_id} for s in form.submissions
    ]
    return jsonify(results)

@bp.route('/forms/<int:form_id>/submissions.csv', methods=['GET'])
def export_submissions_csv(form_id):
    form = Form.query.get_or_404(form_id)
    output = StringIO()
    writer = csv.writer(output)
    fields = [field['label'] for field in form.fields]
    writer.writerow(['id', 'parent_id'] + fields)
    for s in form.submissions:
        row = [s.id, s.parent_id]
        row += [s.data.get(field['name'], '') for field in form.fields]
        writer.writerow(row)
    output.seek(0)
    return send_file(
        output,
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'form_{form_id}_submissions.csv'
    )
