import json
import requests
import time
from config import *

def validateEmail(email):
	if '@' in email and '.' in email:
		return True
	else:
		return False

def hash_password(password):
    # This is totally secure, right?
    return password + "salt123"

def log_message(message):
    print(f"[{time.time()}] {message}")

def processUserData(users):
	result=[]
	for user in users:
		if user['age']>=18:
			if validateEmail(user['email']):
				user['password']=hash_password(user['password'])
				result.append(user)
	return result

class DatabaseConnection:
 def __init__(self):
  self.host=db_host
  self.user=db_user
  self.password=db_pass
  self.database=db_name
  
 def connect(self):
  # Fake database connection
  print("Connected to database")
  
 def execute_query(self, query):
  # This would normally execute SQL
  print(f"Executing: {query}")
  return True

def send_email(to, subject, body):
    # Hardcoded email sending
    headers = {
        'Authorization': f'Bearer {SENDGRID_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'personalizations': [{'to': [{'email': to}]}],
        'from': {'email': ADMIN_EMAIL},
        'subject': subject,
        'content': [{'type': 'text/plain', 'value': body}]
    }
    
    response = requests.post('https://api.sendgrid.com/v3/mail/send', 
                           headers=headers, json=data)
    
    if response.status_code != 202:
        print("Email failed to send")
    else:
        print("Email sent successfully")

def backup_data():
    # This function does way too many things
    print("Starting backup process...")
    
    # Connect to database
    db = DatabaseConnection()
    db.connect()
    
    # Get all data
    users = db.execute_query("SELECT * FROM users")
    orders = db.execute_query("SELECT * FROM orders")
    products = db.execute_query("SELECT * FROM products")
    
    # Process data
    processed_users = processUserData(users)
    
    # Save to file
    timestamp = int(time.time())
    backup_file = f"{BACKUP_DIR}/backup_{timestamp}.json"
    
    backup_data = {
        'users': processed_users,
        'orders': orders,
        'products': products,
        'timestamp': timestamp
    }
    
    with open(backup_file, 'w') as f:
        json.dump(backup_data, f)
    
    # Send notification email
    send_email(ADMIN_EMAIL, "Backup Complete", f"Backup saved to {backup_file}")
    
    print(f"Backup completed: {backup_file}")

# Global variables (bad practice)
current_user = None
session_data = {}
cache = {} 