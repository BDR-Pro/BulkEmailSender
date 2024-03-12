# Bulk Email Sender for Python 📧

Welcome to BulkSender! This is a Python script designed for sending emails in bulk, directly from your terminal. Perfect for newsletters, job applications, event invitations, or any scenario where you need to send personalized emails to a list of recipients. It handles attachments and ensures secure login to your SMTP server, all through a simple and user-friendly interface.

## Features

- Send emails in bulk by leveraging a CSV list of recipients.
- Customize the subject and body of the email for your specific needs.
- Attach files to each email sent – perfect for resumes, reports, or promotional material.
- Utilize environment variables for secure handling of sensitive information like email credentials.
- Simple, clear logging for tracking sent emails.

## Prerequisites

Before you begin, make sure you have the following:

- Python 3.x installed on your machine.
- A `.env` file containing your email credentials (`SENDER_EMAIL` and `SENDER_PASSWORD`).
- A CSV file (`emails.csv`) with the list of recipients' email addresses.
- Any file you wish to attach with your emails, named `cv.pdf` in the script's directory (or modify the script to match your file's name).

## Installation

1. Clone this repository or download the files into your local machine.
2. Install the required packages by running:

   ```bash
   pip install dotenv
   ```

3. Set up your `.env` file in the same directory as the script with the following contents:

   ```env
   SENDER_EMAIL=your_email@gmail.com
   SENDER_PASSWORD=your_password
   ```

## Usage

1. Prepare your `emails.csv` file where each line contains an email address you want to send an email to.
2. If necessary, edit the `subject`, `body`, and `filename` variables in the script to fit your email's subject, body, and the attachment's file name.

3. Run the script:

   ```bash
   python bulksender.py
   ```

4. Check your terminal to monitor the progress. It will print out the status for each email sent.

## Contributing

Feel free to fork the project, make changes, and submit pull requests. If you encounter any issues or have suggestions, please open an issue in the GitHub repository.

## Note

- Ensure you have the correct permissions to send emails to the recipients and that you comply with all legal requirements, including anti-spam laws.
- The script uses Gmail's SMTP server by default. If you're using another email service, modify the `smtp_server` and `port` variables accordingly.

Happy emailing! 📧 🎉
