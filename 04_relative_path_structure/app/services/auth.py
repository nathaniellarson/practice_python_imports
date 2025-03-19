"""
Authentication service.
"""

from typing import Optional
from datetime import datetime

from ..data import Database, User

class AuthService:
    """Authentication service."""
    
    def __init__(self, db: Database):
        """Initialize auth service."""
        self.db = db
    
    def authenticate(self, username: str, password: str) -> Optional[User]:
        """Authenticate user credentials."""
        # Simulate authentication
        if username == "test_user" and password == "password123":
            user = self.db.get_user(1)
            if user:
                user.last_login = datetime.now()
            return user
        return None
    
    def get_current_user(self) -> Optional[User]:
        """Get current authenticated user."""
        # Simulate getting current user
        return self.db.get_user(1) 