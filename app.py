from flask import Flask
from flask_cors import CORS
from config.settings import Config
import os

def create_app(config_class=Config):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    CORS(app)
    
    # Create upload directory if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Register blueprints
    from api.resume_routes import resume_bp
    app.register_blueprint(resume_bp)
    # Note: Payment routes not needed since Razorpay is configured in frontend
    
    # Health check route
    @app.route('/health', methods=['GET'])
    def health_check():
        return {"status": "healthy", "service": "Resume AI Backend"}, 200
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
