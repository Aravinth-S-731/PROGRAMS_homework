#Getting amount from user
rup = int(input("ENTER THE AMOUNT : "))
city = input("ENTER THE CITY : ")
print("YOU LIVE IN "+city+" & YOU HAVE RUPEES : ",rup)

# 3% of budget to fuel exxpense 
fuel = (rup/100)*3;
rup -= fuel

#assigning the price of onioin & tomato according to city
if(city == "chennai"):
    price_onion = 30
elif(city == "trichy"):
    price_onion = 27
else:
    price_onion = 34

price_tomato = 10.5
print(" Since you are in "+city+",The fuel expense is",fuel,"rupees Price of 1kg Onion is ",price_onion,"rupees & Price of 1kg tomato is ",price_tomato,"rupees")

#finding the number of kilos the customer can buy
num = rup/2;
weight_onion = num/price_onion
weight_tomato = num/price_tomato

#rounding off the float to two decimal points
weight_onion = round(weight_onion,2)
weight_tomato = round(weight_tomato,2)
print("\n YOU CAN BUY ",weight_onion,"Kgs OF ONION & ",weight_tomato,"Kgs OF TOMATO.")