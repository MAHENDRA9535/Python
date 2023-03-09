from email.message import EmailMessage
from password import password1
import ssl
import smtplib


email_sender = 'mahendrasai080@gmail.com'
email_password = password1

email_reciever = 'roweso1610@fenwazi.com'

subject = "Dont forget you made a email sender"
body =""" 

when you finmish this let yourself do another project"""

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465,context = context ) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())

