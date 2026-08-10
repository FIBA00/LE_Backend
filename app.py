from flask import Flask, render_template
from flask_cors import CORS
from backend.routes.notes import notes_bp
from backend.routes.code import code_bp

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

app.register_blueprint(notes_bp, url_prefix='/api/notes')
app.register_blueprint(code_bp, url_prefix='/api/code')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
