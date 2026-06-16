"""
AgroBot Flask Application Factory
"""
from flask import Flask
from flask_cors import CORS
from config.config import get_config
from app.utils.logger import setup_logger
from app.routes.health_routes import health_bp
from app.routes.chat_routes import chat_bp
from app.routes.agriculture_routes import agriculture_bp


def create_app(config_name=None):
    """Application factory function"""
    
    # Get configuration
    config = get_config(config_name)
    
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(config)
    
    # Setup logging
    setup_logger(app)
    
    # Setup CORS
    CORS(app, resources={r"/api/*": {"origins": config.CORS_ORIGINS}})
    
    # Register blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(agriculture_bp)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        from flask import jsonify
        return jsonify({
            "status": "error",
            "message": "Resource not found"
        }), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        from flask import jsonify
        app.logger.error(f"Internal server error: {str(error)}")
        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500
    
    # Log app initialization
    app.logger.info(f"AgroBot app initialized with config: {config.__class__.__name__}")
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=10000, debug=True)
