from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'Backend is running!',
        'environment': os.getenv('ENVIRONMENT', 'development')
    })

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        'items': [
            {'id': 1, 'name': 'Item 1', 'description': 'First item'},
            {'id': 2, 'name': 'Item 2', 'description': 'Second item'},
            {'id': 3, 'name': 'Item 3', 'description': 'Third item'}
        ]
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
