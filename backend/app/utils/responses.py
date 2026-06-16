"""
Utility functions for standardized API responses
"""
from flask import jsonify


def success_response(data=None, message="Success", status_code=200):
    """Return a success response"""
    response = {
        "status": "success",
        "message": message,
        "data": data
    }
    return jsonify(response), status_code


def error_response(message="Error", status_code=400, error_code=None):
    """Return an error response"""
    response = {
        "status": "error",
        "message": message
    }
    if error_code:
        response["error_code"] = error_code
    return jsonify(response), status_code


def validation_error_response(errors, status_code=422):
    """Return a validation error response"""
    response = {
        "status": "error",
        "message": "Validation failed",
        "errors": errors
    }
    return jsonify(response), status_code
