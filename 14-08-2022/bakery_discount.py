#intial prices
coffee = 100
vadai = 100
sandwich = 200
coke = 60

#input from user
count_coffee = int(input("ENTER THE QUANTITY OF COFFEE   : "))
count_vadai = int(input("ENTER THE QUANTITY OF VADAI    : "))
count_sandwich = int(input("ENTER THE QUANTITY OF SANDWICH : "))
count_coke = int(input("ENTER THE QUANTITY OF COKE     : "))

#total price for products
price_coffee = count_coffee * coffee
price_vadai = count_vadai * vadai
price_sandwich = count_sandwich * sandwich
price_coke = count_coke * coke
total_price = price_coffee + price_vadai + price_sandwich + price_coke

#if condition for more than one sandwich and mare than 2 vadai
if (count_sandwich > 1) or (count_vadai > 2):
    coke = 50 
    price_coke = count_coke * coke

    #total price for products
    total_price = (price_coffee) + (price_vadai) + (price_sandwich) + (price_coke)
    #the reason for finding the total price after 1st if condition is because there is a price change in the if condition

    print("\nYOU GET A DISCOUNT OF RUPEES 10 FOR YOUR EACH COFFEE")

    #discount after reducing the price of cofee to 50 rupees
    if(count_coffee >= 1) and (count_vadai >= 1) and (count_sandwich >= 1) and (count_coke >= 1):
        total_price = total_price - (total_price * (20/100))
        print("ALSO YOU GET A DISCOUT OF 20 PERCENT FOR ORDERING EACH OF EVERY ITEM")
    elif(total_price > 1000):
        total_price = total_price - (total_price * (20/100))
        print("ALSO YOU GET A DISCOUT OF 20 PERCENT OF YOUR TOTAL AMMOUNT")
    else:
        None

#elif condition to give 20% discount if count of each item is one or greater    
elif (count_coffee >= 1) and (count_vadai >= 1) and (count_sandwich >= 1) and (count_coke >= 1):
    total_price = total_price - (total_price * (20 / 100))

    print("\nSINCE YOU BOUGHT EACH ONE OF EVERY ITEM, YOU GET 20 PERCENT DISCOUNT")

#elif condition to check the total price is greater than 1000 to give 20% discount
elif (total_price > 1000):
    total_price = total_price - (total_price * (20 / 100))
    
    print("\nSINCE YOUR TOTAL IS ABOVE 1000 RUPEES, YOU GET 20 PERCENT DISCOUNT")

else:
    None

#to print the output
print("\nTHE ITEMS PURCHASED ARE:")
print("COFFEE QUANTITY   :",count_coffee," -PRICE :",price_coffee)
print("VADAI  QUANTITY   :",count_vadai," -PRICE :",price_vadai)
print("SANDWICH QUANTITY :",count_sandwich," -PRICE :",price_sandwich)
print("COKE QUANTITY     :",count_coke," -PRICE :",price_coke)

print("\n THE TOTAL PRICE IS : ",total_price)

#---------- OUTPUT ----------
#case 1: NO DISCOUNT
#ENTER THE QUANTITY OF COFFEE   : 3
#ENTER THE QUANTITY OF VADAI    : 2
#ENTER THE QUANTITY OF SANDWICH : 1
#ENTER THE QUANTITY OF COKE     : 0

#THE ITEMS PURCHASED ARE:
#COFFEE QUANTITY   : 3  -PRICE : 300
#VADAI  QUANTITY   : 2  -PRICE : 200
#SANDWICH QUANTITY : 1  -PRICE : 200
#COKE QUANTITY     : 0  -PRICE : 0

 #THE TOTAL PRICE IS :  700
 #----------------------------
 #case 2 : coke price changes to rupees 50
# ENTER THE QUANTITY OF COFFEE   : 0
# ENTER THE QUANTITY OF VADAI    : 2
# ENTER THE QUANTITY OF SANDWICH : 2
# ENTER THE QUANTITY OF COKE     : 1

# YOU GET A DISCOUNT OF RUPEES 10 FOR YOUR EACH COFFEE

# THE ITEMS PURCHASED ARE:
# COFFEE QUANTITY   : 0  -PRICE : 0
# VADAI  QUANTITY   : 2  -PRICE : 200
# SANDWICH QUANTITY : 2  -PRICE : 400
# COKE QUANTITY     : 1  -PRICE : 50

#  THE TOTAL PRICE IS :  650
#----------------------------
#case 3 : discout for each of one item
# ENTER THE QUANTITY OF COFFEE   : 2
# ENTER THE QUANTITY OF VADAI    : 1
# ENTER THE QUANTITY OF SANDWICH : 1
# ENTER THE QUANTITY OF COKE     : 2

# SINCE YOU BOUGHT EACH ONE OF EVERY ITEM, YOU GET 20 PERCENT DISCOUNT

# THE ITEMS PURCHASED ARE:
# COFFEE QUANTITY   : 2  -PRICE : 200
# VADAI  QUANTITY   : 1  -PRICE : 100
# SANDWICH QUANTITY : 1  -PRICE : 200
# COKE QUANTITY     : 2  -PRICE : 120

#  THE TOTAL PRICE IS :  496.0
#----------------------------
#case 3 : discout for total amount greater than 1000
# ENTER THE QUANTITY OF COFFEE   : 2
# ENTER THE QUANTITY OF VADAI    : 3
# ENTER THE QUANTITY OF SANDWICH : 2
# ENTER THE QUANTITY OF COKE     : 4

# YOU GET A DISCOUNT OF RUPEES 10 FOR YOUR EACH COFFEE
# ALSO YOU GET A DISCOUT OF 20 PERCENT OF YOUR TOTAL AMMOUNT

# THE ITEMS PURCHASED ARE:
# COFFEE QUANTITY   : 2  -PRICE : 200
# VADAI  QUANTITY   : 3  -PRICE : 300
# SANDWICH QUANTITY : 2  -PRICE : 400
# COKE QUANTITY     : 4  -PRICE : 200

#  THE TOTAL PRICE IS :  880.0