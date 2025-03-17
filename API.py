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

# Enable CORS with more permissive settings for development
CORS(app, 
     resources={r"/api/*": {
         "origins": ["http://localhost:3000"],
         "methods": ["POST", "OPTIONS"],
         "allow_headers": ["Content-Type"],
         "supports_credentials": True
     }})

# Load environment variables
load_dotenv()

@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def chat():
    # Handle preflight requests
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

    try:
        data = request.json
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Call the workflow function to process the message and get image URL
        image_url = start_workflow(user_message)
        
        response = jsonify({
            'message': 'I have generated a renovation image based on your request.',
            'imageUrl': image_url
        })
        
        # Add CORS headers to the response
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 200

    except Exception as e:
        print(f"Error in /api/chat: {str(e)}")
        error_response = jsonify({'error': str(e)})
        error_response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        error_response.headers.add('Access-Control-Allow-Credentials', 'true')
        return error_response, 500

if __name__ == '__main__':
    print("Server starting on http://localhost:8000")
    app.run(debug=True, port=8000)