'''
Docstring for Student_DataBase_Manageent_System.Student_DB
  
  # Student DB Features
  
  1. Add Student(ID,NAME,AGE,COURSE,MARKS) in JSON file
  2.Display all students
  3.Search student by ID
  4.Update student details
  5.Delete student by ID
  6.Save/load data from file
  7.Menu-based navigation


'''
import json

FILENAME ="student.json"

def load_student():
    try:
        with open(FILENAME,'r') as f :
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def add_student(student) :
    sid = input("Enter Student ID : ")
    name = input("Enter Student Name : ")
    age = input("Enter Student Age : ")
    course = input("Enter Student Course : ")
    marks = input("Enter Student Marks : ")
    student.append({
        "id":sid,
        "name":name,
        "age":age,
        "course":course,
        "marks":marks
    })
    print("Student Added Successfully")
    
def display_student(student):
    if not student:
        print("NO Student Records Found")
        return
    print("\n-------STUDENTS RECORDS-------")
    for s in student:
        print(f'ID : {s['id']}, Name : {s['name']}, Age : {s['age']}, Course : {s['course']}, Marks : {s['marks']}')
        
def  search_student(student) :
    sid = input ("Enter Student ID to Search : ")
    
    for s in student :
        if s['id'] == sid :
            print(f'Found ---> {s}')
            return
    print("Student Records not founded")
    
    
def update_student(student) :
    sid = input("Enter Student ID to Update : ")
    
    for s in student :
        if s['id'] == sid :
            s['name'] = input ("Enter New Name : ")
            s['age'] = input ("Enter New Age : ")
            s['course'] = input("Enter New Course : ")
            s['marks'] = input("Enter New Marks : " )
            print('Student Updated Successfully')
            return
    print("Student Not Founded")
        
def delete_student(student) :
    sid = input("Enter Student ID to Delete : ")
    
    for s in student :
        if s['id'] == sid :
            student.remove(s)
            print('Student Deleted Successfully ')
            return 
    print ("Student Not Founded")
        
           
def save_exit(student) :
    with open(FILENAME,'w') as f :
        json.dump(student,f,indent=4)
        

def main() :
    
    student = load_student()
    
    
    while True:
        print("\n====StudentDB Menu====")
        print("1.Add Students")
        print("2.Display Students")
        print("3.Search Student")
        print("4.Update Student")
        print("5.Delete Student")
        print("6.Save & Exit")
        
        choice = input ("Enter Your Choice (1-6) : ")
        
        if choice == '1':
            add_student(student)
        elif choice == '2':
            display_student(student)
        elif choice == '3':
            search_student(student)
        elif choice == '4':
            update_student(student)
        elif choice == '5':
            delete_student(student)
        elif choice == '6':
            save_exit(student)
            print("Data Saved. Exiting program.")
            break
        else:
            print("Invaild choice! Try again.")
        
main()



