# PyMart Features :
# 1. Show Products
# 2. Add to cart with quantity
# 3. Rempve from cart with quantity
# 4. View cart
# 5. Checkout
# 6. Exit


products = {
    1: {"name": "Apple", "price" : 50},
    2: {"name": "Banana", "price" : 30},
    3: {"name": "Milk", "price" : 60},
    4: {"name": "Bread", "price" : 40},
    5: {"name": "Eggs(dozen)", "price" : 70},
}

cart = {}

wallet = 2000

def show_products():
    print('-----Available Products------')
    for pid,details in products.items():
        print(f'{pid}.{details['name']} - {details['price']}')
        
def view_cart():
    global wallet
    
    print("-----Your Cart-----")
    if not cart :
        print('Cart is Empty')
        print(f'Wallet Balance : {wallet}/-')
    else :
        total = 0
        for pid,item in cart.items():
            name =  item['name']
            price = item['price']
            qty = item['quantity']
            sub_total = qty * price
            total = total + sub_total
            print(f'{pid} | {name} (x{qty}) - {sub_total}/-')
        print(f'Total Cart Amount : {total}/-')
        print(f'Wallet Balance :{wallet}/-')
        

def add_to_cart() :
    global wallet
    
    show_products()
    
    try :
        pid =int(input ("Enter Produt Id to Add : "))
        
        if pid in products:
            qty = int(input("Enter quantity:"))
            cost =products[pid]['price'] * qty
            
            if cost > wallet :
                 print(" Insufficient Wallet Balance")
                 print(f"Wallet Balance: {wallet}/-")
                 return
            wallet -=cost
                
            if pid in cart :
                cart[pid]['quantity'] += qty
            else:
                cart[pid] = {
                    'name' : products[pid]['name'],
                    'price' : products[pid]['price'],
                    'quantity' : qty
                }
                
                print(f'{qty} x {products[pid]['name']} Added into Cart')
                print(f'Amount Deducted : {cost}/-')
                print(f'Remainig Wallet Balance : {wallet}/-')
        else:
            print("Invaild Product")
                
    except ValueError:
        print("Invaild Input")
    
def remove_from_cart() :
    global wallet
    
    view_cart()
    if not cart :
        return
    try :
        pid = int (input("Enter product Id to Remove :"))
        
        if pid in cart :
            qty = int(input("Enter quantity : "))
            current_qty = cart[pid]['quantity']
            price = cart[pid]['price']
            
            if qty == current_qty:
                refund = qty * price
                wallet += refund
                del cart[pid]
                print('Item removed . Refunded {refund}/- \n')
                
            elif qty < current_qty:
                refund = qty * price
                cart[pid]['quantity'] -= qty
                wallet +=refund
                print ("Cart Updated Successfully\n ")
            else:
                print(f'You Only have {current_qty}\n')
                
            print(f'Wallet Balance : {wallet}/-')
        else :
            print("Item not in cart")
        
        
    except ValueError:
        print("Invaild Input")
        
def checkout() :
    view_cart()
    
    if cart :
        confim =input("proceed to Checkout (y/n) : ")
        
        if confim == 'y':
            cart.clear()
            print("Checkout Successfully !")
            print(f'Remaining wallet Balance : {wallet}/-')
            print("Thank You For Shopping at PyMart !")
        else:
            print("Checkout Cancelled\n")
            
       
        

def menu():
    while True:
        
        print("\n====PyMart - Mini Shopping Cart====")
        print("1.View Products")
        print("2.Add to Cart")
        print("3.Remove from Cart")
        print("4. View Cart")
        print("5.Checkout")
        print("6.Exit")
        
        choice = input ("Enter Your Choice (1-6) : ")
        
        if choice == '1':
            show_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3' :
            remove_from_cart()
        elif choice == '4':
            view_cart()
        elif choice == '5':
            checkout()
        elif choice =='6':
            print("Exiting PyMart. Goodbye!")
            break
        else:
            print("Invaild choice ! please try again.")
menu()
        
        
            
        