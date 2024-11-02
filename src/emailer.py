import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_update(smtp_server, smtp_port, email_address, email_password, recipient_email, content):
    # Create a multipart email message
    msg = MIMEMultipart()
    msg["From"] = email_address
    msg["To"] = recipient_email
    msg["Subject"] = "Election News Update from Mr. Fluffy"

    # Attach the content as a MIMEText part
    msg.attach(MIMEText(content, "plain"))

    # Send the email via SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(email_address, email_password)
        server.sendmail(email_address, recipient_email.split(","), msg.as_string())
    
    print("Daily update sent via email.")
