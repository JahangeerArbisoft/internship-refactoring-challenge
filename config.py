# Configuration file - DO NOT COMMIT TO GIT!!!

db_host = "prod-database-01.company.com"
db_user = "admin"
db_pass = "SuperSecretPassword123!"
db_name = "production_db"

# API Keys
STRIPE_SECRET_KEY = "sk_live_1234567890abcdef1234567890abcdef"
SENDGRID_API_KEY = "SG.1234567890abcdef.1234567890abcdef1234567890abcdef"
AWS_ACCESS_KEY = "AKIAI1234567890ABCDEF"
AWS_SECRET_KEY = "1234567890abcdef1234567890abcdef12345678"

# Other sensitive stuff
ADMIN_EMAIL = "admin@company.com"
ADMIN_PASSWORD = "admin123"
JWT_SECRET = "mysupersecretjwtkey"

# Settings
DEBUG = True
TESTING = False
LOG_LEVEL = "DEBUG"

# Hardcoded paths
LOG_FILE = "/var/log/app.log"
UPLOAD_DIR = "/tmp/uploads"
BACKUP_DIR = "/home/user/backups" 