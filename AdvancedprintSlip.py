import subprocess
import os

des = []
qt = []
rat = []
am = []

while True:
    description = input("Enter Description : ")
    qty = int(input("Enter Qty : "))
    rate = int(input("Enter Rate : "))
    amount = qty*rate
    
    des.append(description)
    qt.append(qty)
    rat.append(rate)
    am.append(amount)

    next = input("Another entry ? (y/n) : ")
    if next == 'y' or next == 'Y':
        continue
    elif next == 'n' or next == 'N':
        break
    else:
        print("\n*** Please answer with y or n ***\n")
        

#Printing Section
with open("output.txt", 'w') as f:
    s = "\t=========================\n\tCITY HOSPITAL PHARMA BILL\n\t========================="
    print(s, file=f)
    #print("\033[1m" + s + "\033[0m", file=f)

    print("\n------------------------------------------------", file=f)
    print(f"{'description':>12}{'Qty':>12}{'Rate':>12}{'Amount':>12}", file=f)
    print("------------------------------------------------", file=f)
    for i in range (0,len(qt)):
        print(f"{des[i]:>12}{qt[i]:>12}{rat[i]:>12}{am[i]:>12}", file=f)

    total = 0
    for i in range (0,len(am)):
        total = total + am[i]

    print("\n\t\t\t\t----------------", file=f)
    print(f"{'Total: ':>18}{total:>24}", file=f)

os.startfile("output.txt","print")