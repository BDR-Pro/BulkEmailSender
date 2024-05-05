import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import csv
import os
from dotenv import load_dotenv
import sys
from getpass import getpass
import argparse
import json

# Load environment variables
load_dotenv()
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
smtp_server = "smtp.gmail.com"
port = 465

def print_help():
    print(

    """
    /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
    ( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
    > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
    /\_/\   __  __       _ _   ____                 _              /\_/\ 
    ( o.o ) |  \/  | __ _(_) | / ___|  ___ _ __   __| | ___ _ __   ( o.o )
    > ^ <  | |\/| |/ _` | | | \___ \ / _ \ '_ \ / _` |/ _ \ '__|   > ^ < 
    /\_/\  | |  | | (_| | | |  ___) |  __/ | | | (_| |  __/ |      /\_/\ 
    ( o.o ) |_|  |_|\__,_|_|_| |____/ \___|_| |_|\__,_|\___|_|     ( o.o )
    > ^ <                                                          > ^ < 
    /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
    ( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
    > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
    """

    )
    print("""Welcome to the Email Sender App!

Usage:
    python bulksender.py [command] <arguments>

Commands:
    send    - Execute the send function of the app.
    login   - Perform login operation.

Arguments for 'send':
    -e <path to email CSV file>
    -m <path to message JSON file>
    -a <path to attachment>

Examples:
    python bulksender.py send -e template.csv -m template_message.json -a cv.pdf
    python bulksender.py login abcd@gmail.com
""")

def count_lines(file):
    with open(file, "r") as f:
        return sum(1 for line in f)
    
def send_email(recipient_email, subject, body, filename):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    if filename:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(filename)}")
            message.attach(part)

    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Email sent to {recipient_email}")

def send(emails_file, message_file, attachment):
    with open(message_file, 'r') as file:
        message_data = json.load(file)
        subject = message_data["subject"]
        body = message_data["body"]
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        print(f"Attachment: {attachment}")
        print("Sending emails, please wait...")
    with open(emails_file, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            send_email(row[0], subject, body, attachment)
            print(f"Email sent to {row[0]}")
    print("All emails sent successfully.")
    print("Thank you for using the Email Sender App!")
    #print number of emails sent
    print(f"Total emails sent: {count_lines(emails_file)}")

def login(email):
    password = getpass("Enter your password: ")
    with open(".env", "w") as file:
        file.write(f"SENDER_EMAIL={email}\nSENDER_PASSWORD={password}\n")
    print("Login details saved. You can now use the 'send' command.")

def main():
    parser = argparse.ArgumentParser(description="Bulk Email Sender App")
    parser.add_argument("command", help="Command to execute")
    parser.add_argument("-e", "--emails", help="Path to the email CSV file")
    parser.add_argument("-m", "--message", help="Path to the message JSON file")
    parser.add_argument("-a", "--attachment", help="File path of the attachment")
    args = parser.parse_args()

    if args.command == "send":
        if not all([args.emails, args.message]):
            print("Both -e (emails CSV) and -m (message JSON) are required for the 'send' command.")
            sys.exit(1)
        print("Processing emails, please wait...")
        send(args.emails, args.message, args.attachment)
    elif args.command == "login":
        if len(sys.argv) < 3:
            print("Email address is required for the 'login' command.")
            sys.exit(1)
        login(sys.argv[2])
    else:
        print(f"Unknown command: {args.command}")
        print_help()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_help()
    else:
        main()


