import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SSO_VALIDATION_URL = 'https://example.com/validate_token' 