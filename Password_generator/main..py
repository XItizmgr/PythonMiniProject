import random
import string
passwords = {}
try:
    with open("password.txt",'r') as file:
     for line in file:
         website,pwd = line.strip().split(":")
         passwords[website] = pwd
except: 
    pass
def generate_password():
    char = string.ascii_letters + string.digits + "@"
    password = "".join(random.choice(char) for _ in range(8))
    return password

while True:
    print("\n ___Simple Pasword generator____")
    print("Choose 1 for to add password")
    print("Choose 2 for to view password")
    print("Choose 3 for to check all the password")
    print("Choose 4 for generate random password")
    print("Choose 5 for deleting all password")
    print("Choose 6  for exit")
    
    choice = input("enter your choice : ")
    
    if choice == "1":
        website = input("add website : ")
        password = input("add password : ")
        passwords[website]= password
        with open("password.txt",'a') as file:
            file.write(f"{website}:{password}\n")
        print(f"Password successfully added for {website} website")
    elif choice == "2":
        site = input("Enter the website that u saved password that u want to see : ")
        if site in passwords:
            print(f"The password of given site {site} is {passwords[site]}")
        else:
            print("the given site is not saved")
    elif choice == "3":
        if not passwords:
            print("password is not saved ")
        else:
            for site,pwd in passwords.items():
                print(f"{site}:{pwd}\n")
    elif choice == '4':
        print(f"generated password is {generate_password()}")
    elif choice == '5':
        count = 0
        with open("password.txt",'r')as file:
            for line in file:
                  count += 1
        with open("password.txt",'w') as file:
            print(f"All {count} saved password is deleted")
    elif choice == '6':
        print("thank u for using our password manager")
        break
    else:
        print("plz choose the choice that is given above")
        
    