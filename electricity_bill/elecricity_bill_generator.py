'''
Docstring for electricity_bill.elecricity_bill_generator
'''
'''
Electricity Bill Generator

1) 100 below units -> ₹5 per units
2) 101-200  units -> ₹7 per units
3) 201-300  units -> ₹10 per units
4) 301-400  units -> ₹15 per units

Example 
 78 units -78*5
 105 units-100*5,5units....
'''

def billGenerator(units):
    if units <=100:
        bill =units * 5
    elif units <=200:
        bill = (100 * 5) + ((units -100) * 7)
    elif units <=300:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    else:
        bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 15)
        
    return bill
units=int(input("enter no of units:"))
    
total_bill = billGenerator(units)

print(f'Your total bill is {units}-{total_bill}-/')
    