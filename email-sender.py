# Send emails using Python
# Body of the email comes from the email-body.html file
# Replace all PLACEHOLDERS before running script

# Import libraries
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Setup
html = Template(Path('email-body.html').read_text())
email = EmailMessage()
email['from'] = 'PLACEHOLDER_SENDER_NAME'
email['to'] = 'PLACEHOLDER_RECEPIENT_EMAIL'
email['subject'] = 'PLACEHOLDER_SUBJECT'

# HTML substituttions
html_dict = {'name': 'Jim',
             'species': 'dog',
             'pet': 'Brutus',
             'signature': 'Nick'}
email.set_content(html.substitute(html_dict), 'html')

# Email server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('PLACEHOLDER_SENDER_EMAIL', 'PLACEHOLDER_SENDER_PASSWORD')
    smtp.send_message(email)
    print('Email sent!')
