import re

def validate_name():
    regex = r'[A-Za-z]{2,25}([A-Za-z]{2,25})?'
    fname_flag = False
    lname_flag = False
    print("**Registration**")
    while not fname_flag:
        fname = input("First Name: \n")
        if not len(fname) == 0 and re.fullmatch(regex, fname):
            fname_flag = True
            while not lname_flag:
                lname = input("Last Name: \n")
                if not len(lname) == 0  and re.fullmatch(regex, lname):
                    lname_flag = True
                elif len(lname) == 0 :
                     print("last name should not be empty")
                else:
                    print("invalid name format")
        elif len(fname) == 0:
            print("first name should not be empty")   
        else:
            print("invalid name format")       
    return True
   
def validate_email():
    email_flag = False
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while not email_flag:
        email = input("Email: \n")
        if not len(email) == 0 and re.fullmatch(regex, email):
            email_flag = True
        elif len(email) == 0:
            print("email field should not be empty")
        else:
            print("invalid email format")

    return email

def validate_password():
    password_flag = False
    cpassword_flag = False
    while not password_flag:
       password = input("Password: \n")
       if len(password) >= 6:
           password_flag = True
           while not cpassword_flag:
               cpassword = input("Confirm Password: \n")
               if cpassword == password:
                   cpassword_flag = True
               else:
                   print("password unmatch")
       else:
           print("password too short.. needs to have at least 6 characters")
    return password

def validate_phone():
    phone_flag = False
    regex = r'^01[0125][0-9]{8}$'
    while not phone_flag:
        phone  = input("Phone: \n")
        if not len(phone) == 0 and re.fullmatch(regex, phone):
            phone_flag = True
        elif len(phone) == 0:
            print("phone number field should not be empty")
        else:
            print("invalid phone number format")
    return True



        




   