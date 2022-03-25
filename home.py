from collections import UserString
import inquirer
import json
import registration as reg
import login 
from json.decoder import JSONDecodeError
import projects as p

user = {}
users = []
login_success = False
has_account = False
filename = 'users.json'

def login_check():
    login_success = False
    string = login.login()
    user_info = string.split(",")
    email = user_info[0]
    password = user_info[1]
    with open(filename) as fp:
        try:
            users = json.load(fp)           
        except JSONDecodeError:
            pass
    for u in users:
        if email in u.values() and password in u.values():
            login_success = True
    
    if login_success == True:
        return email
    else:
        print("user doesn't exist. Please re-check your login info")
        login.login()   
  
confirm = {
    inquirer.Confirm('confirmed',
                     message="Welcome to this Crowd-Funding application! Do you have an account?" ,
                     default=True),
}
confirmation = inquirer.prompt(confirm)

if confirmation['confirmed'] == False:
  
    reg.validate_name()
    email = reg.validate_email()
    password = reg.validate_password()
    reg.validate_phone()
    user["email"] = email
    user["password"] = password
    with open(filename) as fp:
        try:
            users = json.load(fp)           
        except JSONDecodeError:
            pass
    for u in users:
        for key in u:
            if key == "email":
                for key in u:
                    if key == "email":
                       if email in u[key]:
                           has_account = True
                           break

    if has_account == False:
        users.append(user)
        with open(filename, "w") as outfile:
           json.dump(users, outfile, indent=4,  separators=(',',': '))
    else:
        print("Already Registered")
   

# def main_menu():
logged_in_user = login_check()
menu_flag = False
while not menu_flag:
     choice = input('''
        Please Choose A Number:
          1) Create A Project
          2) View All Projects
          3) Edit your Project
          4) Delete your Project
          5) Search by Date
          6) Exit
        ''')
     if int(choice) == 1:
       p.create_project(logged_in_user)
     elif int(choice) == 2:
       p.viewProjects()
     elif int(choice) == 3:
       p.editProject(logged_in_user)
     elif int(choice) == 4:
       p.deleteProject(logged_in_user)
     elif int(choice) == 5:
       p.searchByDate()
     elif int(choice) == 6:
       menu_flag = True
   

