import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import csv
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
smtp_server = "smtp.gmail.com"
port = 465

def send_email(recipient_email, subject, body, filename):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Attach a file to the message
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        message.attach(part)

    # Connect to the server and send the email
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Email sent to {recipient_email}")

def main():
    input_file = "emails.csv"
    subject = "Application for Machine Learning and AI Developer Position - Bader Alotaibi"
    body = '''
    Dear Hiring Manager,

    I hope this email finds you well. My name is Bader Alotaibi, and I am reaching out to express my interest in the Machine Learning and AI Developer position within your esteemed organization.

    With a strong foundation in Python, Django, and TensorFlow, coupled with hands-on experience in Rust and machine learning projects, I am well-equipped to contribute effectively to your team. My passion for AI and machine learning, along with my dedication to continuous learning and improvement, drive me to apply the latest techniques and frameworks to solve complex problems.

    You can find samples of my work and projects on my GitHub page: github.com/bdr-pro. I believe these will provide a clear insight into my capabilities and the value I can bring to your team.

    I am enthusiastic about the opportunity to discuss how my education, experience, and skills could be beneficial to your team. I am looking forward to the possibility of contributing to your projects and to the further development of your technology.

    Thank you for considering my application. I am eager to potentially discuss this exciting opportunity with you.

    Warm regards,
    Bader Alotaibi
 
    
    
    '''
    filename = "cv.pdf"

    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader, start=1):
            send_email(row[0], subject, body, filename)
            print(f"{i} - {row[0]}")

if __name__ == "__main__":
    main()
