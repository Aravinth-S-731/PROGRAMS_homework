#intializing the prices
cake_buy = 20
cake_sell = 40
bread_buy = 10
bread_sell = 15
salary = 200 #for each employee 100 (2 employee= 2*100)

#supply of product
supply_cake = int(input("ENTER THE SUPPLY OF CAKE : "))
supply_bread = int(input("ENTER THE SUPPLY OF BREAD : "))

#getting input
count_bread = 0
count_cake = 0
bread = []      #array declaration
cake = []       #array declaration

#for loop to get input in array
for i in range(0,4):
    cnt1 = int(input("Enter the cake nos for customer : "))
    cake.append(cnt1)
    cnt2 = int(input("Enter the bread nos for customer : "))
    bread.append(cnt2)
    count_cake += cake[i]       #count the number of cakes
    count_bread += bread[i]     #count the number of breads
print("NUMBER OF CAKES : ",count_cake)
print("NUMBER OF BREADS: ",count_bread)

print("SUPPLY OF CAKES : ",supply_cake)
print("SUPPLY OF BREADS: ",supply_bread)

while(supply_cake < count_cake | supply_bread < count_bread):
    print("SUPPLY IS LESSER THAN CUSTOMER NEED")
    break

#to check supply with need of product
while(supply_cake >= count_cake & supply_bread  >= count_bread):

    #to find profit
    revenue_cake = count_cake * cake_sell      #price of one cake = 40
    revenue_bread = count_bread * bread_sell    #price of one bread = 15
    profit_cake = revenue_cake - (count_cake * cake_buy)
    profit_bread = revenue_bread - (count_bread * bread_buy)
    total_profit = profit_cake + profit_bread - salary

    #print profit or loss
    if(total_profit > 0):
        print("\n THE PROFIT IF : ",total_profit)
    elif(total_profit < 0):
        print("\n THE LOSS IS : ",total_profit)
    else:
        print("\n NO PROFIT OT LOSS")
    break