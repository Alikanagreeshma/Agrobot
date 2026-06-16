"""
Chat service for managing conversation history and context
"""
from datetime import datetime


class ChatSession:
    """Represents a chat session"""
    
    def __init__(self, session_id=None):
        self.session_id = session_id or self._generate_id()
        self.messages = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def add_message(self, role, content, metadata=None):
        """Add a message to the session"""
        message = {
            "role": role,  # 'user' or 'assistant'
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        self.messages.append(message)
        self.updated_at = datetime.now()
        return message
    
    def get_messages(self):
        """Get all messages in the session"""
        return self.messages
    
    def get_context(self, last_n=5):
        """Get the last N messages for context"""
        return self.messages[-last_n:] if len(self.messages) >= last_n else self.messages
    
    def clear_messages(self):
        """Clear all messages"""
        self.messages = []
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Convert session to dictionary"""
        return {
            "session_id": self.session_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "message_count": len(self.messages),
            "messages": self.messages
        }
    
    def _generate_id(self):
        """Generate a unique session ID"""
        import uuid
        return str(uuid.uuid4())


class ChatService:
    """Service for managing chat sessions"""
    
    def __init__(self):
        self.sessions = {}  # In-memory storage (replace with database in production)
    
    def create_session(self, session_id=None):
        """Create a new chat session"""
        session = ChatSession(session_id)
        self.sessions[session.session_id] = session
        return session
    
    def get_session(self, session_id):
        """Get an existing session"""
        return self.sessions.get(session_id)
    
    def add_message(self, session_id, role, content, metadata=None):
        """Add a message to a session"""
        session = self.get_session(session_id)
        if not session:
            session = self.create_session(session_id)
        
        return session.add_message(role, content, metadata)
    
    def delete_session(self, session_id):
        """Delete a session"""
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False
    
    def get_all_sessions(self):
        """Get all sessions"""
        return {sid: session.to_dict() for sid, session in self.sessions.items()}
