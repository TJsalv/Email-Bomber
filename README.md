📧 SMS/Email Bomber

A simple Python script to send multiple emails to one or more recipients. Designed for testing purposes, notification stress-testing, or educational demonstrations on email automation. Use responsibly.

⚠️ Warning: Sending emails to recipients without their consent is considered spam and may be illegal. Only use this script for testing with your own accounts or recipients who have explicitly allowed you.

Features

Send multiple emails to one or more recipients at once.

Customizable subject and message body.

Retry login on authentication failure.

Clean terminal interface with an ASCII banner.

Requirements

Python 3.x

smtplib (built-in Python library)

Installation

Clone the repository:

git clone https://github.com/yourusername/sms-email-bomber.git
cd sms-email-bomber


Run the script:

python bomber.py

Usage

Enter your email credentials (the script uses Gmail SMTP).

Enter recipient emails separated by space.

Input your email subject and message.

Specify how many times the email should be sent.

Example:

Enter Email: myemail@gmail.com
Enter Password: ********
Enter recipient emails separated by space: test1@example.com test2@example.com
Enter Subject: Test Email
Enter Message: Hello! This is a test.
Times you want to send: 5


The script will send the email 5 times to each recipient.

Important Notes

Make sure Less Secure Apps is enabled for Gmail, or use an App Password for accounts with 2FA.

Avoid sending unsolicited emails. Misuse may lead to your email account being blocked.

This script is intended for educational purposes only.

Screenshot / Preview
  ______                 _ _   ____                  _               
 |  ____|               (_) | |  _ \                | |              
 | |__   _ __ ___   __ _ _| | | |_) | ___  _ __ ___ | |__   ___ _ __ 
 |  __| | '_ ` _ \ / _` | | | |  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|
 | |____| | | | | | (_| | | | | |_) | (_) | | | | | | |_) |  __/ |  
 |______|_| |_| |_|\__,_|_|_| |____/ \___/|_| |_| |_|_.__/ \___|_|  
