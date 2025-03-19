"""
Test configuration and fixtures.
"""

import pytest
from datetime import datetime

from ..app.data import Database, User, AnalyticsEvent
from ..app.services import AuthService, AnalyticsService

@pytest.fixture
def db():
    """Create a test database instance."""
    return Database()

@pytest.fixture
def test_user(db):
    """Create a test user."""
    return User(
        id=1,
        username="test_user",
        created_at=datetime.now(),
        last_login=datetime.now()
    )

@pytest.fixture
def auth_service(db):
    """Create an auth service instance."""
    return AuthService(db)

@pytest.fixture
def analytics_service(db):
    """Create an analytics service instance."""
    return AnalyticsService(db) 