"""
Agriculture recommendation routes blueprint
"""
from flask import Blueprint, request
from app.services.agriculture_service import AgricultureService
from app.utils.responses import success_response, error_response

agriculture_service = AgricultureService()
agriculture_bp = Blueprint("agriculture", __name__, url_prefix="/api/agriculture")


@agriculture_bp.route("/crops", methods=["GET"])
def get_crops():
    """Get list of available crops"""
    try:
        crops = list(agriculture_service.CROP_RECOMMENDATIONS.keys())
        return success_response({
            "crops": crops,
            "total": len(crops)
        }, "Crops retrieved successfully")
    
    except Exception as e:
        return error_response(f"Error retrieving crops: {str(e)}", 500)


@agriculture_bp.route("/crops/<crop_name>", methods=["GET"])
def get_crop_recommendation(crop_name):
    """Get crop recommendation"""
    try:
        result = agriculture_service.get_crop_recommendations(crop_name)
        return success_response(result, "Crop recommendation retrieved successfully")
    
    except Exception as e:
        return error_response(f"Error retrieving crop recommendation: {str(e)}", 500)


@agriculture_bp.route("/fertilizer", methods=["GET"])
def get_fertilizer():
    """Get fertilizer recommendations"""
    try:
        fertilizer_data = agriculture_service.FERTILIZER_RECOMMENDATIONS
        return success_response({
            "recommendations": fertilizer_data
        }, "Fertilizer recommendations retrieved successfully")
    
    except Exception as e:
        return error_response(f"Error retrieving fertilizer recommendations: {str(e)}", 500)


@agriculture_bp.route("/irrigation", methods=["GET"])
def get_irrigation():
    """Get irrigation methods and recommendations"""
    try:
        irrigation_data = agriculture_service.IRRIGATION_RECOMMENDATIONS
        return success_response({
            "methods": irrigation_data
        }, "Irrigation recommendations retrieved successfully")
    
    except Exception as e:
        return error_response(f"Error retrieving irrigation recommendations: {str(e)}", 500)


@agriculture_bp.route("/soil-health", methods=["GET"])
def get_soil_health():
    """Get soil health tips"""
    try:
        soil_health_data = agriculture_service.SOIL_HEALTH
        return success_response({
            "tips": soil_health_data
        }, "Soil health tips retrieved successfully")
    
    except Exception as e:
        return error_response(f"Error retrieving soil health tips: {str(e)}", 500)


@agriculture_bp.route("/pests", methods=["GET"])
def get_pest_management():
    """Get pest management advice"""
    try:
        pest_data = agriculture_service.PEST_MANAGEMENT
        return success_response({
            "advice": pest_data
        }, "Pest management advice retrieved successfully")
    
    except Exception as e:
        return error_response(f"Error retrieving pest management advice: {str(e)}", 500)
