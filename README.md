Ah! I understand now — you want **everything in a single, continuous `README.md`** without extra splits, so it’s one block you can copy-paste. Here’s the fully combined version:

```markdown
# Email Bomber

A Python script to send emails to multiple recipients with customizable subject, message, and number of times to send. Includes input validation, retry login on incorrect credentials, and a simple ASCII banner.

This script allows sending emails to multiple recipients at once. You can set the subject, message, and the number of times to send. It includes retry login if credentials are wrong, input validation to prevent crashes, and cross-platform terminal clearing with a simple ASCII banner.

```

---

\|  ****|               (*) | |  \_ \                | |
\| |**   \_ \_\_ \_\_\_   \_\_ \_ *| | | |*) | \_\_\_  \_ \_\_ \_\_\_ | |*\_   \_\_\_ \_ \_\_
\|  **| | '* ` _ \ / _` | | | |  \_ < / \_ | '* \` \_ | '\_ \ / \_ \ '**|
\| |****| | | | | | (*| | | | | |*) | (*) | | | | | | |*) |  **/ |
|******|*| |*| |*|\_*,*|*|*| |***\_/ \_**/|*| |*| |*|*.**/ \_\_\_|\_|

````

Step-by-step guide to execute:

1. **Install Python**
   - Windows/Linux/macOS:  
     ```bash
     python --version
     ```
     If not installed, download from [python.org](https://www.python.org/downloads/).
   - Termux (Android):  
     ```bash
     pkg update
     pkg upgrade
     pkg install python
     python --version
     ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/EmailBomber.git
   cd EmailBomber
````

* Termux tip: If `git` is not installed:

  ```bash
  pkg install git
  ```

3. **(Optional) Create a virtual environment**

   * Windows/Linux/macOS:

     ```bash
     python -m venv venv
     ```

     Activate:

     * Windows:

       ```bash
       venv\Scripts\activate
       ```
     * Linux/macOS/Termux:

       ```bash
       source venv/bin/activate
       ```

4. **Install required packages**
   No external packages required — uses built-in Python libraries (`smtplib`, `os`, `time`).

5. **Run the script**

   ```bash
   python EmailBomber.py
   ```

   Works on Windows, Linux/macOS, and Termux.

6. **Provide inputs**

   * Enter your email and password.
   * Enter recipient emails separated by commas.
   * Enter subject and message.
   * Enter number of times to send.
     The script will retry login if credentials are incorrect.

7. **Observe output**
   The terminal displays banner and status messages like:

   ```
   Email sent to example@gmail.com! (1/5)
   ```

   It repeats for all recipients and the specified number of times.

8. **Done**
   The script finishes after sending all emails. You can rerun anytime with new inputs.

**Disclaimer:** This script is for educational purposes only. Do not use it for spamming or malicious activity. The author is not responsible for any misuse.

**Tips:** Use `clear_terminal()` in your script for a cleaner output. Never push real credentials to GitHub — use test accounts safely.

```

---

