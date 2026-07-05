"""
Synkora ERP - Development Settings
"""

from .base import *  # noqa
from decouple import config

DEBUG = True

# Django Debug Toolbar
INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE  # noqa: F405

INTERNAL_IPS = ["127.0.0.1"]

# Email - print to console during development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Disable password hashing complexity for faster tests
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
