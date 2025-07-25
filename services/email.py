import requests

def send_email(api_key, from_email, to, subject, body):
    """Send a simple email using SendGrid API"""
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        'personalizations': [{'to': [{'email': to}]}],
        'from': {'email': from_email},
        'subject': subject,
        'content': [{'type': 'text/plain', 'value': body}]
    }

    try:
        response = requests.post(
            'https://api.sendgrid.com/v3/mail/send',
            headers=headers,
            json=data
        )
        
        if response.status_code == 202:
            print("Email sent successfully.")
        else:
            print(f"Failed to send email. Status code: {response.status_code}")
            print("Response:", response.text)

    except Exception as e:
        print("Error while sending email:", str(e))