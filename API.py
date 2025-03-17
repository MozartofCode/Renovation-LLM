# @ Author: Bertan Berker
# @ language: Python
# This is a Flask Backend server that interacts with the frontend and the AI related functions

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from workflow import start_workflow

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

        # Call the workflow function to process the message and get image URL
        image_url = start_workflow(user_message)
        
        response = {
            'message': 'I have generated a renovation image based on your request.',
            'imageUrl': image_url
        }
        
        return jsonify(response), 200

    except Exception as e:
        print(f"Error in /api/chat: {str(e)}")  # Add server-side logging
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Server starting on http://localhost:6000")
    app.run(debug=True, port=6000)