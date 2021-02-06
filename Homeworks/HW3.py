"""
Homework 3

User login application:
    -Get Username and Password values from the user.
    -Check the values in an if statement and tell the user if they were successful.
    
Extra homework is at the bottom of the page.

"""
username , password = "Ugur" , "paSSword1234"

print("____Welcome to the system____")

door = input("Do you have an account? Please enter y/n:")

if door == 'n':
    print("Please create an account!")
    
elif door == 'y':
    username1 = input("Please enter your user name:")
    password1 = input("Please enter your password:")

    if (username != username1 and password == password1):
        print("Invalid user name")
    elif (username == username1 and password != password1):
        print("Invalid password")
    elif (username != username1 and password != password1):
        print("Invalid user name and password")
    else:
        print("Successful login")
        print("Welcome {}".format(username1))
else:
    print("Invalid answer!")

"""
Extra:

Try building the same user application but this time, use a dictionary!
"""

database={'Ugur': 'paSSword1234', 'Meltem': 'paSSword5678'}

print("____Welcome to the system____")

door = input("Do you have an account? Please enter y/n:")

if door == 'n':
    print("Please create an account!")
    
elif door == 'y':
    username = input("Please enter your user name:")
    password = input("Please enter your password:")

    if username in database and database[username] == password:
        print ("Welcome", username)
    elif username in database.items() == None:
        print("Invalid user name")
    elif username in database and database[username] != password:
        print("Invalid password")
    else:
        print("Invalid User name and password ")
else:
    print("Invalid answer!")
    
