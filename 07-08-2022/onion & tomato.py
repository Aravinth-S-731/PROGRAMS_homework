#Getting amount from user
rup = int(input("ENTER THE AMOUNT : "))
print("YOU HAVE RUPEES : ",rup)

#assigning the price of onioin & tomato
price_onion = 2000
price_tomato = 10.5
print("Price of 1kg Onion is ",price_onion," & Price of 1kg tomato is ",price_tomato)

#finding the number of kilos the customer can buy
num = rup/2;
weight_onion = num/price_onion
weight_tomato = num/price_tomato

#rounding off the float to two decimal points
weight_tomato = round(weight_tomato,2)
print("\n YOU CAN BUY ",weight_onion,"Kgs OF ONION & ",weight_tomato,"Kgs OF TOMATO.")