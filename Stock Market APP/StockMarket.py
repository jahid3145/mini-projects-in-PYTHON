'''

#-----STOCK MARKET APPLICATION---
 1) Add money to wallet
 2) Show stock with prices
 3) Stock prices change randomly
 4) Buy stocks if youu have enough money
 5) Sell stocks if you qwn them
 6) Portfoio show yourshares.
 7) wallet updates after buy/sell.
 8) Quit anytime and see final summary. 
'''

import random

wallet = int(input("Enter money into your wallet :"))

stocks ={
    "TATA":100,
    "SUZLON":200,
    "OLA":60

}

portfolio = {}

def update_prices():
    for stock in stocks:
        change = random.randint(-20,20)
        new_price = stocks[stock] +change
        stocks[stock] = max(10,new_price)

while True :
    update_prices()

    print("===== STOCK MARKET =====")
    for name,price in stocks.items():
        print(f'{name} - {price}')
    print(f'Wallet - {wallet}')
    print(f'Portfolio - {portfolio if portfolio else 'Empty'}')
    

    choice = input('\n BUY - B\n SEll - S\n QUIT - Q\n :').lower()
     
    if choice == 'b' :

        stock = input("Enter Stock Name :").upper()
        if stock not in stocks:
            print("Invalid Stock")
            continue
        qty = int(input("How many Shares : "))

        cost = stocks[stock] * qty

        if cost > wallet :
            max_qty = wallet // stocks[stock]
            print(f'Not Enough Money. You can buy max -{max_qty} Shares')
        else :
            wallet -= cost
            portfolio[stock] = portfolio.get(stock,0) + qty
            print(f'Bought {qty} {stock} for {cost}')


    elif choice == 's':

        stock = input ("Enter stock Name : ").upper()
        if stock not in portfolio or portfolio[stock]==0 :
            print("Yoou don't own stock")
            continue

        qty = int(input("How many Shares :"))

        if qty > portfolio[stock]:
            print(f'You only own{portfolio[stock]} Shares')

        else :
            earning = stocks[stock] *qty
            wallet += earning
            portfolio[stock] = portfolio[stock] - qty
            print(f"Sold{qty} {stock} for {earning}")



        
    elif choice == 'q':
        print(f'wallet - {wallet}')
        print(f'portfolio - {portfolio if portfolio else 'Empty'}')
        print("Thanks for Trading")
        break 

        
    else :
        print("Invalid Choice")











