"""
Test configuration and fixtures.
"""

import pytest
from datetime import datetime

from app.data import Database, User, AnalyticsEvent
from app.services import AuthService, AnalyticsService

@pytest.fixture
def db():
    """Database fixture."""
    return Database()

@pytest.fixture
def test_user():
    """Test user fixture."""
    return User(
        id=1,
        username="test_user",
        email="test@example.com",
        created_at=datetime.now(),
        last_login=datetime.now()
    )

@pytest.fixture
def auth_service(db):
    """Auth service fixture."""
    return AuthService(db)

@pytest.fixture
def analytics_service(db):
    """Analytics service fixture."""
    return AnalyticsService(db) 