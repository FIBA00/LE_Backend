from flask import Blueprint, request, jsonify
import os
import json

notes_bp = Blueprint('notes', __name__)

NOTES_DIR = './data/notes'

# Ensure the notes directory exists
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

@notes_bp.route('/save_note', methods=['POST'])
def save_note():
    data = request.get_json()
    note_id = data.get('id')
    content = data.get('content')

    if not note_id or not content:
        return jsonify({'error': 'Note ID and content are required'}), 400

    file_path = os.path.join(NOTES_DIR, f'{note_id}.json')
    try:
        with open(file_path, 'w') as f:
            json.dump({'id': note_id, 'content': content}, f)
        return jsonify({'message': 'Note saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@notes_bp.route('/load_note/<note_id>', methods=['GET'])
def load_note(note_id):
    file_path = os.path.join(NOTES_DIR, f'{note_id}.json')
    if not os.path.exists(file_path):
        return jsonify({'error': 'Note not found'}), 404

    try:
        with open(file_path, 'r') as f:
            note_data = json.load(f)
        return jsonify(note_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@notes_bp.route('/list', methods=['GET'])
def list_notes():
    try:
        notes = [f.replace('.json', '') for f in os.listdir(NOTES_DIR) if f.endswith('.json')]
        return jsonify({'notes': notes}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
