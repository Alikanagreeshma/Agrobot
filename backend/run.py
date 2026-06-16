"""
AgroBot Backend - Main Entry Point
"""
import os
from app import create_app

if __name__ == "__main__":
    # Get environment configuration
    env = os.getenv("FLASK_ENV", "development")
    debug = env == "development"
    
    # Create app
    app = create_app(env)
    
    # Run app
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 10000)),
        debug=debug
    )
