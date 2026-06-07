import json
student_file = "student.json"
try:
    with open(student_file,'r') as file:
       students = json.load(file)
except FileNotFoundError:
    students = {}
        


while True:
    print("\n _______Student Manager Program_______")
    print("Choose 1 for to add Student")
    print("Choose 2 for to view Student")
    print("Choose 3 for to check result")
    print("Choose 4 for to Exit")
    print("Choose 5 for to save it in txt file")
    choice = input("Enter your choice :")
    if choice == "1":
        name = input("Enter the student name :")
        marks = int(input(" Enter the student marks :"))
        students[name] = marks
        print(f"{name} Succesfully added")
        
    elif choice == "2":
        if not students:
            print("no student found")
        else:
            for name,marks in students.items():
                print(f"{name} : {marks}")  
                
    elif choice =="3":
        name = input("Enther the name of the student :") 
        if name in students:
            if students[name] >= 30:
                print(f"{name} is pass")
            else:
                print(f"{name} is not pass")
        else:
            print("the given student name is not on the list")
        
    elif choice == "4":
        with open(student_file, 'w') as file:
            json.dump(students, file)

        print("Data saved.")
        print("Exiting the Software........")
        break
    elif choice =="5":
     with open(student_file,'w') as file:
           json.dump(students, file)
    
    else:
        print("plz choose the choices that are given above")
        
                 