
#! Project Name-Currency Convertor
#! Author-Rahul
#! Location-Mars
#! Date-24-05-2022
import time
with open('currency.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

while(True):
    print("PRESS '0' TO QUIT!!!!!!")
    try:
        amount = int(input("Enter the amount: "))
    except:
        print("Enter a valid amount!!!!!!")
        time.sleep(3)
        break
    if amount == 0:
        print("****************** THANKS FOR USING CURRENCY CONVERTOR ******************")
        time.sleep(3)
        break
    print("Enter the name of the curreny in which you want to convert amount:")
    print("*************************** Available Options ***************************")
    [print(item) for item in currencyDict.keys()]
    try:
        currency = input("Please enter any of the values:\n")
        print(
            f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")
    except:
        print("Enter a valid Currency!!!")
        time.sleep(3)
        break
