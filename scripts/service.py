import requests

#Lets create a dummy database to analyze mocking

database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}


def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

#This was a sample api fetch functionality. Similarly we can use mocking with Database manipulation, 
# and other external functonality like using some erternal servers to send and receive data. 


#Mocking SMTP email sending function

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(smtp_server, smtp_port, from_addr, to_addr, subject, body):
    """
    This function actually sends the email if it is called with proper parameter and the email and password are set correctly.
    But since as we are only focused on testing the functionality not how the smtp server works neither we are
    concerned with testing the smtp library. Thu we mock the different called parts and tests the working of the functionality
    in our codebase
    """
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_addr, "dummyPassword")
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    
    server.quit()
    
    