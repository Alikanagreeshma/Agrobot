"""
Logging utility for AgroBot
"""
import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(app):
    """Setup logging configuration"""
    log_level = os.getenv("LOG_LEVEL", "INFO")
    log_file = os.getenv("LOG_FILE", "agrobot.log")
    
    # Create logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    log_path = os.path.join("logs", log_file)
    
    # File handler
    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=10485760,  # 10MB
        backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    ))
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    ))
    
    # Configure app logger
    if not app.logger.handlers:
        app.logger.addHandler(file_handler)
        app.logger.addHandler(console_handler)
    
    app.logger.setLevel(getattr(logging, log_level))
    
    return app.logger


def get_logger(name):
    """Get a logger instance"""
    return logging.getLogger(name)
