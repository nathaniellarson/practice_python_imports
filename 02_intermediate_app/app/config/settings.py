"""
Application configuration settings.
"""

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class DatabaseConfig:
    """Database configuration settings."""
    host: str = "localhost"
    port: int = 5432
    database: str = "myapp"
    user: str = "admin"
    password: Optional[str] = None

@dataclass
class AppConfig:
    """Main application configuration."""
    debug: bool = False
    api_key: Optional[str] = None
    database: DatabaseConfig = field(default_factory=DatabaseConfig)

# Global configuration instance
config = AppConfig() 