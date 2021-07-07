import smtplib
from email.message import EmailMessage
from email.parser import BytesParser, Parser
from email.policy import default

Email_Address = 'chenyan20210705@gmail.com'
Email_Password = 'oqlpkmymmiqwjuuw'
contacts = ['cyan72427@gmail.com', Email_Address]

msg = EmailMessage()
msg['Subject'] = 'Notification: Finished the Survey'
msg['From'] = Email_Address
msg['To'] = contacts
msg.set_content('Dear Employee, \n\nPlease finished this survey by 8th July \n\nSincerely, \nChen Yan ')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(Email_Address,Email_Password)
    smtp.send_message(msg)
    
# Testing code 
# with smtplib.SMTP('smtp.gmail.com', 1025) as smtp:
#     subject = 'Notification: Finished the Survey  '
#     body = 'How about dinner at 6pm this Saturday'

#     msg = f'Subject:{subject}\n\n{body}'

#     smtp.sendmail(Email_Address, Email_Address,msg)
# Run command Line : (base) chenyan@ChenYan ~ % python3 -m smtpd -c DebuggingServer -n localhost:1025


# Tutorial Link : https://www.youtube.com/watch?v=JRCJ6RtE3xU