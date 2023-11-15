import os
import smtplib
import ssl
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import dotenv 
from jinja2 import Environment, FileSystemLoader

dotenv.load_dotenv()

# SMTP configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
username = os.getenv('SMTP_USERNAME')
password = os.getenv('SMTP_PASSWORD')
sender_email = os.getenv('SENDER_EMAIL')

# load the jinja2 environment
jinja_env = Environment(loader=FileSystemLoader('templates'))
template = jinja_env.get_template('demo.html')

# reading the csv containing email contacts using pandas
contacts = pd.read_csv('email.csv')


# connect to the smtp server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    try:
        server.starttls()
        server.login(username, password)
    
        # iterate throught the email list
        for index, contact in contacts.iterrows():
             # extracting user information
             first_name = contact['FirstName']
             last_name = contact['LastName']
             email = contact['Email']
        
             # generating a personalized email
             email_content = template.render(name=first_name, surname=last_name)
        
             # create MIME message
             msg = MIMEMultipart()
             msg['From'] = sender_email
             msg['To'] = contact['Email']
             msg['Subject'] = 'noGenEmailer'
             msg.attach(MIMEText(email_content, 'html'))
        
             # send Email
             server.sendmail(sender_email, contact['Email'], msg.as_string())
        
             print(f'Email sent successfully to {email}.')
    except Exception as e:
        print(f"Something happened while trying to send email: {e}")
    