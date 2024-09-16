import random, os
import smtplib
from email.message import EmailMessage


try:
    with open('private/gmail_server_account/gmail.txt', 'r') as file:
        my_gmail = file.read()
except:
    my_gmail = None
    print("Your gmail file not found")
    
try:
    with open('private/gmail_server_account/password.txt', 'r') as file:
        my_password = file.read()
except: 
    my_password = None
    print("Your password file not found")    


users = {
    'sumit8393' : 'iamtrynow@gmail.com',
    # 'sumit8393' : 'iamtrynow@gmail.com',
}

def create_OTP():
    return random.randrange(111111, 999999)

def send_gmail(receiver_gamil:str, subject:str, message:str):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(my_gmail, my_password)
        email = EmailMessage()
        email['From'] = "MSK Institute"
        email['To'] = receiver_gamil
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)
        print(f"OTP send success")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server.quit()

def verify():
    while True:
        os.system('cls')
        user_name = input('Enter username: ')
        try:
            if user_name in users.keys():
                otp = create_OTP()
                receiver_gmail = users[user_name]
                subject = "OTP for login form python program."
                message = f"Please do not share OTP anyone : \n Your OTP: {otp}"
                send_gmail(receiver_gmail, subject, message)   
                print("OTP send in your gmail.")
                return otp
                break
        except:
            print("Can't find user: (create new accout)")

def log_In():
    otp = verify()
    while True:
        user_otp = input('Enter OTP: ')
        if user_otp == str(otp):
            print("Login Success:")
            break
        else:
            print("\n\nOTP invaild :")
            print("\n Please enter Valid OTP: ")   


log_In()