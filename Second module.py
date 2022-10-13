# import of libraries
import pandas as pd
import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# Please fill data below with your email, password and email recipient
email_from = ''
password = ''
# Email can be sent to multiple recipients
email_to = ''


# Define the HTML document, including hyperlink to webpage from which we get information

html = '''
    <html>
        <body>
            <h1>Daily TESLA stock price report</h1>
            <p>Hello, welcome to your daily report!</p>    
            
             <p>For further information visit <a href="https://finance.yahoo.com/quote/TSLA?p=TSLA!">TSLA</a></p> 
            <img src='cid:myimageid' width="1000">
        </body>
    </html>
    '''
#

# Define a function to attach files as MIMEApplication to the email
    # Add another input extra headers default to None
#
def attach_file_to_email(email_message, filename, extra_headers=None):
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Set up the input extra_headers for img
      # Default is None: since for regular file attachments, it's not needed
      # When given a value: the following code will run
         # Used to set the cid for image
    if extra_headers is not None:
        for name, value in extra_headers.items():
            file_attachment.add_header(name, value)
    # Attach the file to the message
    email_message.attach(file_attachment)
#

# Code to include today's date to use in topic of our mail, we can change order of
# printing information (day, month, year)

date_str = pd.Timestamp.today().strftime('%d-%m-%Y')

# Code to create class for sender, receiver and subject of the message
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Report email - {date_str}'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))

# Attach documents to message, by default it's our chart in png format, and csv file

attach_file_to_email(email_message, 'TSLA13102022.png', {'Content-ID': '<myimageid>'})
#
attach_file_to_email(email_message, 'TSLA_report.csv')
#

# Convert it as a string
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_from, password)
    server.sendmail(email_from, email_to, email_string)
