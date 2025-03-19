"""
Data models for the application.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    """User model."""
    id: int
    username: str
    email: str
    created_at: datetime
    last_login: Optional[datetime] = None

@dataclass
class AnalyticsEvent:
    """Analytics event model."""
    id: int
    user_id: int
    event_type: str
    timestamp: datetime
    metadata: dict 