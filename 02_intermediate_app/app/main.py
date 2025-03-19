"""
Main application module.
"""

from app.data import Database
from app.services import AuthService, AnalyticsService

def main():
    """Main application entry point."""
    # Initialize services
    db = Database()
    auth_service = AuthService(db)
    analytics_service = AnalyticsService(db)
    
    # Simulate user authentication
    user = auth_service.authenticate("test_user", "password123")
    if user:
        print(f"Welcome, {user.username}!")
        
        # Track login event
        analytics_service.track_event(
            user=user,
            event_type="login",
            metadata={"ip": "127.0.0.1"}
        )
        
        # Get user's events
        events = analytics_service.get_user_events(user)
        print(f"Recent events: {len(events)}")
        for event in events:
            print(f"- {event.event_type} at {event.timestamp}")
    else:
        print("Authentication failed!")

if __name__ == "__main__":
    main() 