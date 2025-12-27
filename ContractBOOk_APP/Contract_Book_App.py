'''
Docstring for ContractBOOk_APP.Contract_Book_App

contact Book Features:
1.Add contact(name,phone,email)
2.View contact
3.Update contact
4.Delete contact
5.Search contact
6.Count total contact
7.Exit contact
'''

contact = {}

def Add_Contact():
    name=input("Enter your name :").strip()
    if name in contact :
        print("Contact already Exists")
    else:
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email: ").strip()
        contact[name]= {'phone':phone,'email':email}
        print('Contact Added Successfully')
        
def View_Contact():
    if contact:
        print('----Contact List-----')
        for name,info in contact.items():
            print(f'Name:{name},Phone:{info['phone']},Email:{info['email']}')
    else:
        print("No Contact Found")
        
def Update_Contact():
    name = input("Enter The Name To Update: ").strip()
    if name in contact:
        print("Leave blank to keep old value")
        phone = input(f'New Phone ({contact[name]['phone']}): ').strip()
        email = input(f'New Email ({contact[name]['email']}): ').strip()
        
        if phone:
            contact[name]['phone'] = phone
        if email:
            contact[name]['email'] = email
        print("Contact Update Successfully")
        
    else:
        print("No Contact Found")
        
def Delete_Contact():
     
    name = input ("Enter The Name To Delete Contact: ").strip()
    if name in contact:
         del contact[name]
         print("Contact Deleted Successfully")
    else:
        print("Contact Not Found")
        
def Search_Contact():
    name = input('Enter The Name To Search Contact : ').strip()
    if name in contact:
        print(f'Name:{contact[name]}, Phone :{contact[name]['phone']}, Email:{contact[name]['email']}')
    else:
        print("Contact Not Found")

def Count_Contact():
    print(f"Total No of Contact Are:{len(contact)}")
        
          
def menu():
    while True:
        print('==== Contact Book Menu ====')
        print('1. Add Contact')
        print('2. View Contact')
        print('3. Update Contact')
        print('4. Delete Contact')
        print('5. Search Contacts')
        print('6. Count Contacts')
        print('7. Exit')
        
        choice = input("Enter your choice(1 - 7):").strip()
        if choice == '1':
            Add_Contact()
        elif choice == '2':
            View_Contact()
        elif choice == '3':
            Update_Contact()
        elif choice == '4':
            Delete_Contact()
        elif choice == '5':
            Search_Contact()
        elif choice == '6':
            Count_Contact()
        elif choice == '7':
            print("Exiting Contact Book>> Good Bye!")
            break
        else:
            print('Invaild Choice')
            
menu()
    
        
        