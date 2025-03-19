"""
Authentication service tests.
"""

import pytest
from datetime import datetime

from ..app.services import AuthService
from ..app.data import User

def test_authenticate_success(auth_service):
    """Test successful authentication."""
    user = auth_service.authenticate("test_user", "password123")
    assert user is not None
    assert user.username == "test_user"
    assert isinstance(user.last_login, datetime)

def test_authenticate_failure(auth_service):
    """Test failed authentication."""
    user = auth_service.authenticate("wrong_user", "wrong_password")
    assert user is None

def test_get_current_user(auth_service):
    """Test getting current user."""
    user = auth_service.get_current_user()
    assert user is not None
    assert user.username == "test_user" 