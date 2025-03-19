"""
Database tests.
"""

import pytest
from datetime import datetime

from app.data import Database, User, AnalyticsEvent

def test_database_connection(db):
    """Test database connection."""
    assert db.connected is True

def test_get_user(db):
    """Test retrieving user."""
    user = db.get_user(1)
    assert user is not None
    assert user.username == "test_user"
    assert isinstance(user.created_at, datetime)

def test_get_nonexistent_user(db):
    """Test retrieving nonexistent user."""
    user = db.get_user(999)
    assert user is None

def test_save_event(db):
    """Test saving analytics event."""
    event = AnalyticsEvent(
        id=1,
        user_id=1,
        event_type="test",
        timestamp=datetime.now(),
        metadata={"test": "data"}
    )
    success = db.save_event(event)
    assert success is True 