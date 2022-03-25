import re
import json
from json.decoder import JSONDecodeError
import inquirer

def create_project(user):
    project = {}
    projects = []
    filename = 'projects.json'
    print("**Create Project**")
    string = validate_title_details()
    project_info = string.split(",")
    title = project_info[0]
    details = project_info[1]
    target = validate_target()
    date_string = validate_date()
    date_info = date_string.split(":")
    start_date = date_info[0]
    end_date = date_info[1]
    project["title"] = title
    project["details"] = details
    project["target"] = target
    project["start-date"] = start_date
    project["end-date"] = end_date
    project["owner"] = user
    with open(filename) as fp:
        try:
            projects = json.load(fp)           
        except JSONDecodeError:
            pass
    
    projects.append(project)
    with open(filename, "w") as outfile:
         json.dump(projects, outfile, indent=4,  separators=(',',': '))
    print("Project Created")
 
     
def viewProjects():
    filename = 'projects.json'
    projects = []
    print("**View Projects**")
    with open(filename) as fp:
        try:
            projects = json.load(fp)           
        except JSONDecodeError:
            pass
    for p in projects:
       print("\n")
       for key in p:
           print(key,": ", p[key])


def deleteProject(user):
    check_delete = True
    filename = 'projects.json'
    projects = []
    print("**Delete My Project**")
    with open(filename) as fp:
        try:
            projects = json.load(fp)           
        except JSONDecodeError:
            pass
    for p in projects:
       for key in p:
           if(p[key]== user):
               for key in p:
                   print(key, ":", p[key])
    get_project = input("which project do you want to delete?")
    confirm = {
        inquirer.Confirm('confirmed',
        message="Are you sure you want to delete your project?" ,
        default=True),
        }
    confirmation = inquirer.prompt(confirm)
    if confirmation['confirmed'] == True:
        for i in range(len(projects)):
            if projects[i]["owner"] == user and projects[i]["title"] == get_project:
                projects.pop(i)
                break
            else:
                check_delete = False

        if check_delete == False:
            print("no project with that name")
        else:
            print("deleted successfully")
        with open(filename, "w") as outfile:
            json.dump(projects, outfile, indent=4,  separators=(',',': '))
       
    else:
        print("nothing deleted")
      

def searchByDate():
    date_flag = False
    filename = 'projects.json'
    regex = r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$'
    while not date_flag:
        date = input("Enter Date")
        if not len(date) == 0 and re.fullmatch(regex, date):
            date_flag = True
            with open(filename) as fp:
              try:
                 projects = json.load(fp)           
              except JSONDecodeError:
                 pass
            for p in projects:
                for key in p:
                    if(p["start-date"]== date or p["end-date"]== date):
                        print(key, ":", p[key])


        elif len(date) == 0:
            print("date should not be empty")
        else:
            print("invalid date format")


    if len(date) == 0:
        print("Date should not be empty")
    


def editProject(user):
    check_val  = 0
    filename = 'projects.json'
    projects = []
    print("**Edit My Project**")
    with open(filename) as fp:
        try:
            projects = json.load(fp)           
        except JSONDecodeError:
            pass
    project_title = input("which project do you want to edit?")
    choice = input('''
        Please Choose The Field you want to edit:
          1) Title
          2) Details
          3) Target
          4) Start Date
          5) End Date
          6) Go To Main Menu
        ''')
    if int(choice) == 1:
        check_val = 1
    elif int(choice) == 2:
        check_val = 2
    elif int(choice) == 3:
        check_val = 3
    elif int(choice) == 4:
        check_val = 4
    elif int(choice) == 5:
        check_val = 5
   
    edit_success = False
    value = input("Enter new value\n")
    for p in projects:
       for key in p:
           if(p[key]== user):
                for key in p:
                    if p["title"] == project_title:
                      if check_val == 1:
                        p["title"] = value
                      elif check_val ==2:
                        p["details"] = value
                      elif check_val ==3:
                        p["target"] = value
                      elif check_val == 4:
                          p["start-date"] = value
                      elif check_val == 5:
                          p["end-date"] = value
                      edit_success = True
    with open(filename, "w") as outfile:
        json.dump(projects, outfile, indent=4,  separators=(',',': '))
    if edit_success == True:
        print("edited successfully")
    else:
        print("no project with that name")
  

def validate_title_details():
    pname_flag = False
    details_flag = False
    project_info=''
    regex = r'^[a-zA-Z0-9_ ]*$'
    while not pname_flag:
        pname = input("Title: \n")
        if not len(pname) == 0 and re.fullmatch(regex, pname):
            project_info += pname
            pname_flag = True
            while not details_flag:
                details = input("Details: \n")
                if not len(details) == 0 and re.fullmatch(regex, details):
                    details_flag = True
                    project_info += ","
                    project_info += details
                elif len(details) == 0:
                     print("details should not be empty")
                else:
                    print("Invalid Format")
        elif len(pname) == 0:
            print("title should not be empty") 
        else:
            print("Invalid format")         
    return project_info

def validate_target():
    target_flag = False
    regex = r'[0-9]+'
    while not target_flag:
        target = input("target: \n")
        if not len(target) == 0 and re.fullmatch(regex, target):
            target_flag = True
        elif len(target) == 0:
            print("target field should not be empty")
        else:
            print("invalid target format")
    return target

def validate_date():
    s_date_flag = False
    e_date_flag = False
    date_info = ""
    regex = r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$'
    while not s_date_flag:
        start_date = input("Start Date: \n")
        if not len(start_date) == 0 and re.fullmatch(regex, start_date):
            s_date_flag = True
            date_info += start_date
            while not e_date_flag:
                end_date = input("End Date: \n")
                if not len(end_date) == 0 and re.fullmatch(regex, end_date):
                    e_date_flag = True
                    date_info += ":"
                    date_info += end_date
                elif len(end_date) == 0:
                    print("end date field should not be empty")
                else:
                    print("end date target format")
                
        elif len(start_date) == 0:
            print("date field should not be empty")
        else:
            print("date target format")
    return date_info
        



