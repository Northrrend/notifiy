import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

smtp_srv = ''
from_addr = 'from@email.com'
to_addrs = [
    'a@email.com',
    'b@email.com'
]
msg = MIMEText('message')
subject = 'subject'
msg['Subject'] = Header(subject, 'utf-8')

smtpObj = smtplib.SMTP(smtp_srv, 25)
smtpObj.sendmail(from_addr, to_addrs, msg.as_string())
