from json.decoder import JSONDecodeError
import json

users = []
def login():
    filename = 'users.json'
    login_info=''
    login_success = False
    login_flag = False
    email_flag = False
    password_flag = False
    
    print("**Login**")
    while not email_flag:
        email = input("Email: \n")
        if not len(email) == 0:
            email_flag = True
            login_info += email
            while not password_flag:
                password = input("Password: \n")
                if len(password) >= 6:
                    password_flag = True
                    login_info += ","
                    login_info += password

                elif len(password) == 0:
                    print("password should not be empty")
                else:
                    print("Invalid password format. Password too short..")
        else:
            print("email should not be empty")
    return login_info
        
    