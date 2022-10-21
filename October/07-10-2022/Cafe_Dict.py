menu = { #MENU ITEMS WITH COST AND STOCK DETAILS
    "vadai": {
        'price': 10,
        'inventory': 50,
        'min_count': 10,
        'reorder': 30
    },
    "cake": {
        'price': 20,
        'inventory': 30,
        'min_count': 5,
        'reorder': 10
    },
    "coffee": {
        'price': 15,
        'inventory': 100,
        'min_count': 30,
        'reorder': 50
    }
}

sales_info = {  #SALES INFO DICTIONARY
    'vadai':{
        'count_sold': 0,
        'cost_sold_for': 0,
        'remaining': 0
    },
    'cake':{
        'count_sold': 0,
        'cost_sold_for': 0,
        'remaining': 0
    },
    'coffee':{
        'count_sold': 0,
        'cost_sold_for': 0,
        'remaining': 0
    }
}
no_of_restocks,max_restock = 0,5    #intial restock and Restock limit
total_cost = 0                      #total limit

def print_menu():                   #funtion to print the menu
    print("MENU")
    for key in menu.keys():         #print menu
        print(key)

def main_fun():                     #main function to calculate sales
    global no_of_restocks           #global variable
    option = "y"
    while option == "y" and no_of_restocks <= max_restock:  #when user want to continue and within restock limit
        item_needed = input("\nWhat do you want : ")
        if item_needed in menu.keys():                      #check item in menu
            quantity = int(input("Enter thr quantity : "))  #if there get quantity

            if quantity <= menu[item_needed]['inventory']:  #if entered quantity is less than limit
                sales_info[item_needed]['count_sold'] += quantity   #add quantity to sales info
                menu[item_needed]['inventory'] -= quantity          #sub quantity from inventory
                sales_info[item_needed]['cost_sold_for'] = (quantity * menu[item_needed]['price'])  #calculate price
                print("Remainig Quantity : ",menu[item_needed]['inventory'])    #print remaining quantity

                if menu[item_needed]['inventory'] <= menu[item_needed]['min_count']: #if inventory is low
                    menu[item_needed]['inventory'] += menu[item_needed]['reorder']  #restock inventory
                    no_of_restocks += 1                                             #increment resctock count
                    print("Reordered: ",item_needed," Reorder Quantity: ",menu[item_needed]['reorder'])
            else:
                print("You have order above available quantity. Enter quantity below: ",menu[item_needed]['inventory'])
        else:
            print("ENTER A VALID ITEM IN MENU")
        option = input("DO YOU WANT TO CONTIUE  (y/n) : ")  #whether user want to continue
    if no_of_restocks > max_restock:    #stop calcluation if limit reached
        print("YOU PURCHASED FIVE TIMES. THANK YOU!")

def print_sales_info():             #function to print sales info
    global total_cost,sales_info
    for index in sales_info.keys(): #to print sales info of all items in menu
        print("ITEM : ",index,"\tSOLD QUANTITY : ",sales_info[index]['count_sold'],"\tFOR TOTAL COST OF : ",sales_info[index]['cost_sold_for'],"\tREMAINING : ",menu[index]['inventory'])
        total_cost += sales_info[index]['cost_sold_for'] #total cost of all items
    print("\n\tTOTAL SALES AMOUNT : ",total_cost)
    print("\tNUMBER OF RESTOCKS : ",no_of_restocks)

print_menu()
main_fun()
print_sales_info()

"""
---------- OUTPUT:1 ----------
MENU
vadai
cake
coffee

What do you want : cake
Enter thr quantity : 30
Remainig Quantity :  0
Reordered:  cake  Reorder Quantity:  10
DO YOU WANT TO CONTIUE  (y/n) : y

What do you want : vadai
Enter thr quantity : 20
Remainig Quantity :  30
DO YOU WANT TO CONTIUE  (y/n) : y

What do you want : coffee
Enter thr quantity : 10
Remainig Quantity :  90
DO YOU WANT TO CONTIUE  (y/n) : n
ITEM :  vadai   SOLD QUANTITY :  20     FOR TOTAL COST OF :  200        REMAINING :  30
ITEM :  cake    SOLD QUANTITY :  30     FOR TOTAL COST OF :  600        REMAINING :  10
ITEM :  coffee  SOLD QUANTITY :  10     FOR TOTAL COST OF :  150        REMAINING :  90

        TOTAL SALES AMOUNT :  950
        NUMBER OF RESTOCKS :  1
---------- OUTPUT:2 ----------
MENU
vadai
cake
coffee

What do you want : cake
Enter thr quantity : 35
You have order above available quantity. Enter quantity below:  30
DO YOU WANT TO CONTIUE  (y/n) : n
ITEM :  vadai   SOLD QUANTITY :  0      FOR TOTAL COST OF :  0  REMAINING :  50
ITEM :  cake    SOLD QUANTITY :  0      FOR TOTAL COST OF :  0  REMAINING :  30
ITEM :  coffee  SOLD QUANTITY :  0      FOR TOTAL COST OF :  0  REMAINING :  100

        TOTAL SALES AMOUNT :  0
        NUMBER OF RESTOCKS :  0
"""