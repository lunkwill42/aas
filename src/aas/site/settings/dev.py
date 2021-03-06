from .base import *

DEBUG = get_bool_env("DEBUG", True)
TEMPLATES[0]["OPTIONS"]["debug"] = get_bool_env("TEMPLATE_DEBUG", True)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "secret-secret!"


FRONTEND_URL = "http://localhost:3000"

CORS_ORIGIN_WHITELIST = [
    FRONTEND_URL,
    "http://127.0.0.1:3000",
]


# Prints sent emails to the console
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
