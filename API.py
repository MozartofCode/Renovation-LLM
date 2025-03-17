# @ Author: Bertan Berker
# @ language: Python
# This is a Flask Backend server that interacts with the frontend and the AI related functions

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)
# Enable CORS with additional options
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000"], "methods": ["POST", "OPTIONS"]}})

# Load environment variables
load_dotenv()

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # TODO: Add your AI function calls here
        # For now, we'll return a mock response
        response = {
            'message': 'I understand your request about: ' + user_message,
            'imageUrl': 'https://placehold.co/600x400'  # Using a placeholder image for testing
        }
        
        return jsonify(response), 200

    except Exception as e:
        print(f"Error in /api/chat: {str(e)}")  # Add server-side logging
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Server starting on http://localhost:5000")  # Add startup message
    app.run(debug=True, port=5000)