import psutil  # importing psutil to get CPU usage from pypi
import smtplib  # for sending emails
import time  # for loop delay
import os  # Add this import at the top
from email.mime.text import MIMEText  # for email formatting

def send_email(subject, body, to_email, from_email, password, smtp_server, smtp_port):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def get_cpu_usage():
    cpu_threshold = int(input("Enter CPU usage threshold percentage: "))
    check_interval = 60  # seconds between checks
    # Email configuration (replace with your details)
    from_email = 'kishorpatil2107@gmail.com'
    password = os.getenv('GMAIL_PASSWORD')  # Read from environment variable
    if not password:
        raise ValueError("GMAIL_PASSWORD environment variable not set")
    to_email = 'kishordpatil2107@gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    while True:
        print("Fetching CPU usage...")
        current_cpu_usage = psutil.cpu_percent(interval=1)
        if current_cpu_usage > cpu_threshold:
            alert_msg = f"Alert! CPU usage is at {current_cpu_usage}%, which is above the threshold of {cpu_threshold}%"
            print(alert_msg)
            send_email("CPU Usage Alert", alert_msg, to_email, from_email, password, smtp_server, smtp_port)
        else:
            print(f"CPU usage is at {current_cpu_usage}%, which is within the safe limit of {cpu_threshold}%")
        time.sleep(check_interval)

get_cpu_usage()