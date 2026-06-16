"""
Health check routes blueprint
"""
from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/", methods=["GET"])
def index():
    """Home endpoint"""
    return jsonify({
        "status": "success",
        "message": "AgroBot API is running!",
        "version": "1.0.0"
    }), 200


@health_bp.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "AgroBot",
        "version": "1.0.0"
    }), 200
