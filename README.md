# 📧 Bulk Email Sender (SMTP Demo)

> ⚠️ **Disclaimer:** This tool is for educational and internal testing purposes only. Do not use it to spam, harass, or target individuals without their explicit consent. Misuse may violate email service terms and local laws.

A Python script that demonstrates how to send multiple emails using Gmail's SMTP server. Designed for devs, testers, and curious minds who want to explore how SMTP works under the hood.

---

## 🚀 Features

- 🔐 Login via Gmail SMTP (`smtp.gmail.com:587`)
- 📬 Send custom messages to multiple recipients
- 🔁 Loop-based sending with progress output
- 🖼 ASCII banner for terminal flair
- 🧼 Clears terminal between steps for clean UX

---

## 🛠 Requirements

- Python 3.x
- Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) enabled
- Internet connection

---

## 📦 Installation Guide

### 💻 On Desktop (Windows/Linux/macOS)

1. **Clone the repository**

   ```bash
   git clone https://github.com/TJsalv/Email-Bomber.git
   cd email_bomber

   ```

2. **Install Python (if not already installed)**  
   Download from [python.org](https://www.python.org/downloads/) and ensure it's added to your system PATH.

3. **Run the script**

   ```bash
   python email_bomber.py
   ```

---

### 📱 On Android (Termux)

1. **Install Termux from F-Droid**  
   [https://f-droid.org/en/packages/com.termux/](https://f-droid.org/en/packages/com.termux/)

2. **Update and install Python**

   ```bash
   pkg update && pkg upgrade
   pkg uninstall python
   pkg install python
   ```

3. **Fix SSL Support (Required for Gmail SMTP)**  
   If you get an error like `RuntimeError: No SSL support included in this Python`, do the following:

   ```bash
   pkg install openssl
   pkg reinstall python
   ```

   Then verify SSL is working:

   ```bash
   python
   >>> import ssl
   >>> ssl.OPENSSL_VERSION
   ```

   You should see something like `OpenSSL 3.x.x`. If not, SSL is still broken.

4. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/email_bomber.git
   cd email_bomber
   ```

5. **Run the script**

   ```bash
   python email_bomber.py
   ```

> 🔐 **Note:** Gmail may block sign-ins from Termux unless you use [App Passwords](https://support.google.com/accounts/answer/185833?hl=en). Regular passwords often trigger security blocks.
---

## 🧪 Usage

You'll be prompted to:

1. Enter your Gmail address and password
2. Input recipient emails (space-separated)
3. Define subject and message
4. Choose how many times to send each message

Example:

```
Enter Email: yourname@gmail.com
Enter Password: ********
Enter recipient emails separated by space: test1@example.com test2@example.com
Enter Subject: Hello from SMTP
Enter Message: This is a test message.
Times you want to send: 3
```

---

## 🧠 Educational Purpose

This script helps you understand:

- SMTP authentication and TLS handshake
- Email header formatting
- Loop-based message dispatching

---

## 🧹 Notes

- Gmail may block sign-ins from less secure apps. Use [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) for safer access.
- This script does not support HTML formatting or attachments.
- ASCII banner is purely aesthetic. Feel free to customize it.

---

## 🙋‍♂️ Author

Built by [Tristan](https://github.com/TJsalv) — for testing, learning, and experiment only


