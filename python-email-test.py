import smtplib
import os

# Define your email settings as repo secrets
sender_email = os.environ['GMAIL_SENDER']
receiver_email = os.environ['GMAIL_RECIPIENT']
# in case you want to send to another email
receiver_email2 = os.environ['GMAIL_RECIPIENT_2']
# password of the sender email
password = os.environ['GMAIL_APP_PW'] # https://myaccount.google.com/apppasswords


def send_email():
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        subject = "python email test"
        body = "Just testing\n\n"
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, message)
        server.sendmail(sender_email, receiver_email2, message)
        print("Email sent!")
        server.quit()
    except Exception as e:
        print(f"Email error: {str(e)}")

send_email()
