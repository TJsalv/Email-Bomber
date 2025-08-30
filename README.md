# Email Bomber

A Python script to send emails to multiple recipients with customizable subject, message, and number of times to send. Includes input validation, retry login on incorrect credentials, and a simple ASCII banner.

This script allows sending emails to multiple recipients at once. You can set the subject, message, and the number of times to send. It includes retry login if credentials are wrong, input validation to prevent crashes, and cross-platform terminal clearing with a simple ASCII banner.

---

## Banner

| | () | | _ \ | |
| | _ __ ___ __ _ | | | |) | ___ _ __ ___ | |_ ___ _ __
| | | ' _ \ / _ | | | | _ < / _ | ' ` _ | '_ \ / _ \ '|
| || | | | | | (| | | | | |) | () | | | | | | |) | / |
||| || ||_,||| |_/ _/|| || ||./ ___|_|

yaml
Copy code

---

## Features

- Send emails to **multiple recipients** at once.
- Set **subject**, **message**, and **number of times** to send.
- **Retry login** if the email/password is wrong.
- Input validation to prevent crashes from invalid inputs.
- Cross-platform terminal **clearing** and banner display.

---

## Step-by-Step Execution Guide

### 1. Install Python

- **Windows/Linux/macOS:**
```bash
python --version
If not installed, download from python.org.

Termux (Android):

bash
Copy code
pkg update
pkg upgrade
pkg install python
python --version
2. Clone the Repository
bash
Copy code
git clone https://github.com/YOUR_USERNAME/EmailBomber.git
cd EmailBomber
Termux tip: If git is not installed:

bash
Copy code
pkg install git
3. (Optional) Create a Virtual Environment
Windows/Linux/macOS:

bash
Copy code
python -m venv venv
Activate:

Windows:

bash
Copy code
venv\Scripts\activate
Linux/macOS/Termux:

bash
Copy code
source venv/bin/activate
4. Install Required Packages
No external packages required — uses built-in Python libraries (smtplib, os, time).

5. Run the Script
bash
Copy code
python EmailBomber.py
(Works on Windows, Linux/macOS, and Termux)

6. Provide Inputs
Enter your email and password.

Enter recipient emails separated by commas.

Enter subject and message.

Enter number of times to send.

The script will retry login if credentials are incorrect.

7. Observe Output
The terminal displays banner and status messages like:

css
Copy code
Email sent to example@gmail.com! (1/5)
It repeats for all recipients and the specified number of times.

8. Done
The script finishes after sending all emails. You can rerun anytime with new inputs.

Disclaimer
This script is for educational purposes only. Do not use it for spamming or malicious activity. The author is not responsible for any misuse.

Tips
Use clear_terminal() in your script for a cleaner output.

Never push real credentials to GitHub — use test accounts safely.
