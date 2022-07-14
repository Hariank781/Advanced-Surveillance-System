import smtplib

EMAIL_FROM = 'diptonilroy_cs20.rvitm@rvei.edu.in'
EMAIL_TO = ['kuldeepjain_cs20.rvitm@rvei.edu.in', 'diptonilr@gmail.com']

import smtplib
import imghdr

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send():
    from_address = EMAIL_FROM
    to_address = EMAIL_TO[1]
    message = MIMEMultipart('Security Alert')
    message['Subject'] = 'Security Alert'
    message['From'] = from_address
    message['To'] = to_address
    content = MIMEText('We have encountered an unrecognised person. What would you like us to do?', 'plain')
    message.attach(content)
    with open('Unrecognised1.jpg', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        print(file_type)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(from_address, 'Rsst12345')
    mail.sendmail(from_address,to_address, message.as_string())
    mail.close()