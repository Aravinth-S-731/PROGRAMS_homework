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

#elif condition to give 20% discount if count of each item is one or greater    
elif (count_coffee >= 1) and (count_vadai >= 1) and (count_sandwich >= 1) and (count_coke >= 1):
    total_price = total_price - (total_price * (20 / 100))

#elif condition to check the total price is greater than 1000 to give 20% discount
elif (total_price > 1000):
    total_price = total_price - (total_price * (20 / 100))

else:
    None

#to print the output
print("\nTHE ITEMS PURCHASED ARE:")
print("COFFEE QUANTITY   :",count_coffee," -PRICE :",price_coffee)
print("VADAI  QUANTITY   :",count_vadai," -PRICE :",price_vadai)
print("SANDWICH QUANTITY :",count_sandwich," -PRICE :",price_sandwich)
print("COKE QUANTITY     :",count_coke," -PRICE :",price_coke)

print("\n THE TOTAL PRICE IS : ",total_price)