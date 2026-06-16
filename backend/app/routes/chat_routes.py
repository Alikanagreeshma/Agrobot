"""
Chat routes blueprint
"""
from flask import Blueprint, request
from app.services.agriculture_service import AgricultureService
from app.services.chat_service import ChatService
from app.utils.responses import success_response, error_response

# Initialize services
agriculture_service = AgricultureService()
chat_service = ChatService()

# Create blueprint
chat_bp = Blueprint("chat", __name__, url_prefix="/api/chat")


@chat_bp.route("", methods=["POST"])
def send_message():
    """Send a message and get a response"""
    try:
        data = request.get_json()
        
        if not data:
            return error_response("No data provided", 400)
        
        message = data.get("message", "").strip()
        session_id = data.get("session_id", "default")
        
        if not message:
            return error_response("Message cannot be empty", 400)
        
        # Add user message to session
        chat_service.add_message(session_id, "user", message)
        
        # Get AI response
        ai_response = agriculture_service.get_ai_response(message)
        
        # Extract response text
        if "response" in ai_response:
            response_text = ai_response["response"]
        elif "recommendations" in ai_response:
            response_text = f"Here's information about {ai_response.get('crop', 'your crop')}: {ai_response['recommendations']}"
        elif "guidance" in ai_response:
            response_text = f"Here's guidance: {ai_response['guidance']}"
        elif "advice" in ai_response:
            response_text = f"Here's advice about {ai_response.get('topic', 'this topic')}: {ai_response['advice']}"
        else:
            response_text = str(ai_response)
        
        # Add bot response to session
        chat_service.add_message(session_id, "assistant", response_text)
        
        return success_response({
            "session_id": session_id,
            "message": message,
            "response": response_text,
            "full_response": ai_response
        }, "Message processed successfully")
    
    except Exception as e:
        return error_response(f"Error processing message: {str(e)}", 500)


@chat_bp.route("/session/<session_id>", methods=["GET"])
def get_session(session_id):
    """Get chat session history"""
    try:
        session = chat_service.get_session(session_id)
        
        if not session:
            return error_response("Session not found", 404)
        
        return success_response(session.to_dict(), "Session retrieved successfully")
    
    except Exception as e:
        return error_response(f"Error retrieving session: {str(e)}", 500)


@chat_bp.route("/session/<session_id>", methods=["DELETE"])
def clear_session(session_id):
    """Clear chat session"""
    try:
        session = chat_service.get_session(session_id)
        
        if not session:
            return error_response("Session not found", 404)
        
        session.clear_messages()
        return success_response({"session_id": session_id}, "Session cleared successfully")
    
    except Exception as e:
        return error_response(f"Error clearing session: {str(e)}", 500)


@chat_bp.route("/sessions", methods=["GET"])
def get_all_sessions():
    """Get all chat sessions"""
    try:
        sessions = chat_service.get_all_sessions()
        return success_response(sessions, "Sessions retrieved successfully")
    
    except Exception as e:
        return error_response(f"Error retrieving sessions: {str(e)}", 500)
