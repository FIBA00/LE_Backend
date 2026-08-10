from flask import Blueprint, request, jsonify
import os

code_bp = Blueprint('code', __name__)

CODE_DIR = './data/code'

# Ensure the code directory exists
if not os.path.exists(CODE_DIR):
    os.makedirs(CODE_DIR)

@code_bp.route('/list', methods=['GET'])
def list_code_files():
    try:
        files = [f for f in os.listdir(CODE_DIR) if os.path.isfile(os.path.join(CODE_DIR, f))]
        return jsonify({'files': files}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@code_bp.route('/load/<filename>', methods=['GET'])
def load_code_file(filename):
    file_path = os.path.join(CODE_DIR, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return jsonify({'filename': filename, 'content': content}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@code_bp.route('/save', methods=['POST'])
def save_code_file():
    data = request.get_json()
    filename = data.get('filename')
    content = data.get('content')

    if not filename or not content:
        return jsonify({'error': 'Filename and content are required'}), 400

    file_path = os.path.join(CODE_DIR, filename)
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return jsonify({'message': 'File saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
