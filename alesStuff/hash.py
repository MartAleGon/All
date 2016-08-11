from hashlib import *

#The above will give a hash of MYSTRING
#first=input("What is your first name?") 
#last=input("What is your last name?")



    
def entry(database):
    action = input("Please enter LOGIN or SIGNUP \n")
    if action == "SIGNUP":
        signup(database)
        entry(database)
    if action == "LOGIN":
        login(database)
        exit = ""
    
    while exit != "EXIT":
        exit = input("\n")

def signup():
    user=input("What is your username? \n")
    pas=input("What is your password? \n")
    hash=sha256(pas.encode('utf-8')).hexdigest()
    signup = {user: hash}
    

def out(database):
    act=input("Please log out \n")
    

def login():
    user=input("What is your username? \n")
    pas=input("What is your password? \n")
    
def signup():
    user=input("What is your username? \n")
    pas=input("What is your password? \n")
    hash=sha256(pas.encode('utf-8')).hexdigest()
    signup = {user: hash}

    
