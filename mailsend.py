import yagmail
import os
from dotenv import load_dotenv
load_dotenv()
def mail_bhejo(recipient_email, subject, body, file_to_send):
    sender_email = os.getenv("email")
    sender_password = os.getenv("passwd")  
    yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(
        to=recipient_email,
        subject=subject,
        contents=body,
        attachments=file_to_send
    )