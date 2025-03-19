"""
Analytics service tests.
"""

import pytest
from datetime import datetime

from ..app.services import AnalyticsService
from ..app.data import AnalyticsEvent

def test_track_event(analytics_service, test_user):
    """Test tracking an analytics event."""
    success = analytics_service.track_event(
        user=test_user,
        event_type="test_event",
        metadata={"test": "data"}
    )
    assert success is True

def test_get_user_events(analytics_service, test_user):
    """Test retrieving user events."""
    events = analytics_service.get_user_events(test_user)
    assert len(events) > 0
    assert isinstance(events[0], AnalyticsEvent)
    assert events[0].user_id == test_user.id
    assert events[0].event_type == "login" 