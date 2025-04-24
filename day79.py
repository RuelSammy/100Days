import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email, from_email, app_password):
    """
    Sends an email using Gmail's SMTP server.

    Args:
        subject (str): Email subject line.
        body (str): Email body content.
        to_email (str): Recipient email address.
        from_email (str): Sender's email address.
        app_password (str): App password for sender's email.
    """
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_email, app_password)
            smtp.send_message(msg)
            print(f"Email sent to {to_email}!")
    except Exception as e:
        print(f"Failed to send email. Reason: {e}")

# Example usage
if __name__ == "__main__":
    send_email(
        subject="Test Email from Python",
        body="Hello! This is a test email sent using Python.",
        to_email="recipient@example.com",
        from_email="your_email@gmail.com",
        app_password="your_app_specific_password"  # NOT your regular Gmail password
    )
