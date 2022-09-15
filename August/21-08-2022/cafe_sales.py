#initial values
dish = ["PUFFS","CAKE","BREAD","COFFEE","COKE"]
cost = [20,30,30,15,30]
start_supply = [50,50,50,70,100]
end_supply = start_supply.copy()
items_sold = []
transaction = 10
customer = 0
option = "y"
noofdishes = len(dish)

#loop to get values from user
while(customer <= transaction):
    if(option == "n"):
        break
    customer += 1   #to count the customers
    for i in range(0,noofdishes):
        if(end_supply[i] > 0):  #condition to check the supply 
            no_of_items = int(input( str(dish[i])+ " COSTS RUPEES : " +str(cost[i])+ " HOW MANY DO U WANT : "))
            if(end_supply[i] - no_of_items >= 0):
                end_supply[i] -= no_of_items
            else:
                print("NOT ENOUGH QUANTITY")
        else:
            print(dish[i]," IS SOLD OUT")
    #input given by user to continue or end
    option = input("REMAINING TRANSACTIONS " +str(transaction - customer)+ " DO U WANT TO CONTINUE (y/n) : ")

print("\n")
#to print the sales and remaining of the cafe
for i in range(0,noofdishes):
    temp_var = start_supply[i] - end_supply[i]
    items_sold.append(temp_var)
    print(dish[i],"\tSOLD :",items_sold[i]," -REMAINING :",end_supply[i],"\t,INCOME IS : Rs.",cost[i] * items_sold[i])

# ---------- OUTPUT ----------
# PUFFS COSTS RUPEES : 20 HOW MANY DO U WANT : 10
# CAKE COSTS RUPEES : 30 HOW MANY DO U WANT : 9
# BREAD COSTS RUPEES : 30 HOW MANY DO U WANT : 8
# COFFEE COSTS RUPEES : 15 HOW MANY DO U WANT : 7
# COKE COSTS RUPEES : 30 HOW MANY DO U WANT : 6
# REMAINING TRANSACTIONS 9 DO U WANT TO CONTINUE (y/n) : y
# PUFFS COSTS RUPEES : 20 HOW MANY DO U WANT : 9
# CAKE COSTS RUPEES : 30 HOW MANY DO U WANT : 8
# BREAD COSTS RUPEES : 30 HOW MANY DO U WANT : 7
# COFFEE COSTS RUPEES : 15 HOW MANY DO U WANT : 6
# COKE COSTS RUPEES : 30 HOW MANY DO U WANT : 5
# REMAINING TRANSACTIONS 8 DO U WANT TO CONTINUE (y/n) : n


# PUFFS   SOLD : 19  -REMAINING : 31      ,INCOME IS : Rs. 380
# CAKE    SOLD : 17  -REMAINING : 33      ,INCOME IS : Rs. 510
# BREAD   SOLD : 15  -REMAINING : 35      ,INCOME IS : Rs. 450
# COFFEE  SOLD : 13  -REMAINING : 57      ,INCOME IS : Rs. 195
# COKE    SOLD : 11  -REMAINING : 89      ,INCOME IS : Rs. 330
# ---------- OUTPUT ----------
# PUFFS COSTS RUPEES : 20 HOW MANY DO U WANT : 40
# CAKE COSTS RUPEES : 30 HOW MANY DO U WANT : 40
# BREAD COSTS RUPEES : 30 HOW MANY DO U WANT : 40
# COFFEE COSTS RUPEES : 15 HOW MANY DO U WANT : 40
# COKE COSTS RUPEES : 30 HOW MANY DO U WANT : 40
# REMAINING TRANSACTIONS 9 DO U WANT TO CONTINUE (y/n) : y
# PUFFS COSTS RUPEES : 20 HOW MANY DO U WANT : 10
# CAKE COSTS RUPEES : 30 HOW MANY DO U WANT : 11
# NOT ENOUGH QUANTITY
# BREAD COSTS RUPEES : 30 HOW MANY DO U WANT : 5
# COFFEE COSTS RUPEES : 15 HOW MANY DO U WANT : 5
# COKE COSTS RUPEES : 30 HOW MANY DO U WANT : 5
# REMAINING TRANSACTIONS 8 DO U WANT TO CONTINUE (y/n) : n


# PUFFS   SOLD : 50  -REMAINING : 0       ,INCOME IS : Rs. 1000
# CAKE    SOLD : 40  -REMAINING : 10      ,INCOME IS : Rs. 1200
# BREAD   SOLD : 45  -REMAINING : 5       ,INCOME IS : Rs. 1350
# COFFEE  SOLD : 45  -REMAINING : 25      ,INCOME IS : Rs. 675
# COKE    SOLD : 45  -REMAINING : 55      ,INCOME IS : Rs. 1350