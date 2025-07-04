import logging
import os

logger = logging.getLogger()

# Use local SQLite DB
SQLALCHEMY_DATABASE_URI = 'sqlite:////app/superset_home/superset.db'

# Secret key is required
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY')

# Log level
log_level_text = os.getenv("SUPERSET_LOG_LEVEL", "INFO")
LOG_LEVEL = getattr(logging, log_level_text.upper(), logging.INFO)

# Optional minimal features
FEATURE_FLAGS = {
    "ALERT_REPORTS": False,
}

# Optional frontend settings (harmless even if unused)
WEBDRIVER_BASEURL_USER_FRIENDLY = "http://localhost:8088/"

# Disable Cypress/test config and Docker config import (not needed in your case)
