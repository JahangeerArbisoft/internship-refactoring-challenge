import time
import json
from config.config import BACKUP_DIR, ADMIN_EMAIL, SENDGRID_API_KEY
from services.email import send_email
from utils import process_user_data
from database.connection import DatabaseConnection  

def get_all_data():
    """Fetch users, orders, and products from the database."""
    db = DatabaseConnection()
    db.connect()

    users = db.execute_query("SELECT * FROM users")
    orders = db.execute_query("SELECT * FROM orders")
    products = db.execute_query("SELECT * FROM products")

    return users, orders, products

def save_backup_to_file(data: dict) -> str:
    """Save backup data to JSON file and return filename"""
    timestamp = int(time.time())
    filename = f"{BACKUP_DIR}/backup_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(data, f)

    return filename

def send_notification_email(backup_file: str):
    """Send email about successful backup."""
    subject = "Backup Completed"
    body = f"Backup saved to file: {backup_file}"

    send_email(
        api_key=SENDGRID_API_KEY,
        from_email=ADMIN_EMAIL,
        to=ADMIN_EMAIL,
        subject=subject,
        body=body
    )

def backup_data():
    print("Starting backup process...")

    users, orders, products = get_all_data()

    processed_users = process_user_data(users)

    backup_data_dict = {
        "users": processed_users,
        "orders": orders,
        "products": products,
        "timestamp": int(time.time())
    }

    backup_file = save_backup_to_file(backup_data_dict)

    send_notification_email(backup_file)

    print(f"Backup completed successfully: {backup_file}")
