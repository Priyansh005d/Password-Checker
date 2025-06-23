password = (input("Enter your Password : "))
with open("password.txt") as f:                   #opens the txt file
    secret = f.read()
    if(password == secret):                       #checks if password is correct
        print("Correct Password")
        print("You may proceed further...")
    else:
        print("Incorrect password")
        print("Access Denied")    
