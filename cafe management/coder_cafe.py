#PYTHON MINI PROJECT-CAFE MANAGEMENT SYSTEM
#Step1 :greeting the customer
#Step2 :displaying the menu{'piza':100,'burger':80,'coffee':50,'tea':30}
#step3 : note the item
#step4 : check the item in our menu
#        if yes "add the cost"
#              ask user for anythin else
#            if yes: note the second item
#                check the item i our menu
#                        claculate total cost and display
#             if no: end order & dxisplay cost
#        if no : "sorry we dont have that item"


menu = {
    'pizza': 100,
    'burger': 80,
    'coffee': 50,
    'tea': 20,
    'chicken puff': 60
}

print("Welcome to Coder Cafe")
print("Here is our menu")
print("pizza:100\nburger:80\ncoffee:50\ntea:20\nchicken puff:60")

order_item = input("Enter the item you want to order: ").lower()

order_total=0

if order_item in menu:
    order_total+=menu[order_item]
    order=input('Do you want anything else(Yes/NO)')
    if order=="Yes".lower():
        order_item2 = input('enter a 2nd item : ')
        if order_item2 in menu:
            order_total +=menu[order_item2]
            print(f'Your order value{order_total}')
    else:
        print(f'your order value:{order_total}')
    
else:
    print("you enter a wrong item")
    





