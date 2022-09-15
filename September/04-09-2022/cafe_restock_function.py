"""
Write an app for the cafe. Calculate the sales for the day. 
Use a function to calculate each customer sale. Also, Use the function to restock the supply of items if the supply 
goes down to 20% of the original supply. Print how many times the supply was restocked. 
Also print the total numbers of items sold.
"""
cafe_items = ["VADAI","COFFEE","CAKE"]  #cafe menu
length = len(cafe_items)                #count of items
price_items = [10,15,20]                #price of items 
sales_amount = [0,0,0]                  #income at the end of the day
total_amount = 0                        #total amount earned
initial_supply = [100,100,100]          #intial supply
count_supply = [0,0,0]                  #quatity bought by customers
restock_count = 0                       #number of times restocked
option = "y"                            #whether user want to continue
print("MENU : ",*cafe_items)            #cafe menu

def restockitems():                     #function to restock items
    global restock_count,initial_supply #global variables to change values outside the function for each & every time called
    restock_count += 1                  #increment once for each restock
    initial_supply = [100,100,100]      #reset the initial supply
    return initial_supply,restock_count

def sales(count_supply):                #to get quantity from user
    for index in range (0,length):      
        current_countofitem = 0         #temporary variable to get the quatity from user
        current_countofitem += int(input("ENTER THE QUANTITY OF "+cafe_items[index]+": "))
        count_supply[index] += current_countofitem      #adding the quantity of each items
        initial_supply[index] -= current_countofitem    #subtracting the quantity from supply
    return count_supply,initial_supply
while (option == "y"):                                  #while user want to continue
    if (restock_count < 3):                    #only restock 3 times, if the restock is more than three times the close the shop
        for index in range(0,length):           #calling the function to restock the supply
            if (initial_supply[index] <= 20):   #if supply goes down to 20% restock
                restockitems()                  #calling restockitems() function
        sales(count_supply)                     #calling sales() funtion
        option = input("CONTINUE (y/n) : ")     #getting option from user to continue or stop
    else:                                       #if the restock count is above three times stop restocking
        option = "n"
        print("----RESTOCK UNAVILABLE----")
for index in range(0,length):           #to calculate the sales at the end of the day 
    sales_amount[index] = price_items[index] * count_supply[index]
    total_amount += sales_amount[index]
print("\tSALES INFO")   #printing the sales information
print("NUMBER OF TIMES RESTOCKED : ",restock_count)
print("TOTAL INCOME FROM CAFE : ",total_amount)
for index in range(0,length):
    print(cafe_items[index]+"\t:SOLD :",count_supply[index],",FOR :",sales_amount[index],",REMAINING :",initial_supply[index])
"""
---------- OUTPUT:1 ----------
MENU :  VADAI COFFEE CAKE
ENTER THE QUANTITY OF VADAI: 90
ENTER THE QUANTITY OF COFFEE: 70
ENTER THE QUANTITY OF CAKE: 60
CONTINUE (y/n) : y
ENTER THE QUANTITY OF VADAI: 50
ENTER THE QUANTITY OF COFFEE: 60
ENTER THE QUANTITY OF CAKE: 70
CONTINUE (y/n) : n
        SALES INFO
NUMBER OF TIMES RESTOCKED :  1
TOTAL INCOME FROM CAFE :  5950
VADAI   :SOLD : 140 ,FOR : 1400 ,REMAINING : 50
COFFEE  :SOLD : 130 ,FOR : 1950 ,REMAINING : 40
CAKE    :SOLD : 130 ,FOR : 2600 ,REMAINING : 30
---------- OUTPUT:2 ----------
MENU :  VADAI COFFEE CAKE
ENTER THE QUANTITY OF VADAI: 10
ENTER THE QUANTITY OF COFFEE: 11
ENTER THE QUANTITY OF CAKE: 5
CONTINUE (y/n) : y
ENTER THE QUANTITY OF VADAI: 4
ENTER THE QUANTITY OF COFFEE: 2
ENTER THE QUANTITY OF CAKE: 15
CONTINUE (y/n) : n
        SALES INFO
NUMBER OF TIMES RESTOCKED :  0
TOTAL INCOME FROM CAFE :  735
VADAI   :SOLD : 14 ,FOR : 140 ,REMAINING : 86
COFFEE  :SOLD : 13 ,FOR : 195 ,REMAINING : 87
CAKE    :SOLD : 20 ,FOR : 400 ,REMAINING : 80
---------- OUTPUT:3 ----------
MENU :  VADAI COFFEE CAKE
ENTER THE QUANTITY OF VADAI: 90
ENTER THE QUANTITY OF COFFEE: 60
ENTER THE QUANTITY OF CAKE: 60
CONTINUE (y/n) : y
ENTER THE QUANTITY OF VADAI: 90
ENTER THE QUANTITY OF COFFEE: 60
ENTER THE QUANTITY OF CAKE: 60
CONTINUE (y/n) : y
ENTER THE QUANTITY OF VADAI: 90
ENTER THE QUANTITY OF COFFEE: 60
ENTER THE QUANTITY OF CAKE: 60
CONTINUE (y/n) : y
ENTER THE QUANTITY OF VADAI: 90
ENTER THE QUANTITY OF COFFEE: 60
ENTER THE QUANTITY OF CAKE: 60
CONTINUE (y/n) : y
----RESTOCK UNAVILABLE----
        SALES INFO
NUMBER OF TIMES RESTOCKED :  3
TOTAL INCOME FROM CAFE :  12000
VADAI   :SOLD : 360 ,FOR : 3600 ,REMAINING : 10
COFFEE  :SOLD : 240 ,FOR : 3600 ,REMAINING : 40
CAKE    :SOLD : 240 ,FOR : 4800 ,REMAINING : 40
"""