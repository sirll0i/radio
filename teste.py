import smtplib
from email.mime.text import MIMEText

sender_email = "your_verified_sendgrid_email@example.com"
api_key = "YOUR_SENDGRID_API_KEY"

msg = MIMEText("This is a test email")
msg["Subject"] = "Test"
msg["From"] = sender_email
msg["To"] = "receiver@example.com"

server = smtplib.SMTP("smtp.sendgrid.net", 587)
server.starttls()
server.login("apikey", api_key)  # Note: username is literally "apikey"
server.send_message(msg)
server.quit()