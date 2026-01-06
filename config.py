# config.py
import os

class Config:
    SECRET_KEY = 'safelens-secret-key-2025-change-this-in-production'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:2653@localhost:5432/Safelens_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 🔴 YOUR ACTUAL GOOGLE CREDENTIALS
    GOOGLE_CLIENT_ID = '339906825102-ndpnjjg2n7vrhh4vi25rpfm5ckfgilup.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = ''  # You need to get this from Google Console
    GOOGLE_DISCOVERY_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    
    # Flask-Mail Configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'sleepyn3mu@gmail.com'  # Your Gmail
    MAIL_PASSWORD = '12345678'  # Google App Password
    MAIL_DEFAULT_SENDER = 'sleepyn3mu@gmail.com'

# Export for easy import
GOOGLE_CLIENT_ID = Config.GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = Config.GOOGLE_CLIENT_SECRET
GOOGLE_DISCOVERY_URL = Config.GOOGLE_DISCOVERY_URL