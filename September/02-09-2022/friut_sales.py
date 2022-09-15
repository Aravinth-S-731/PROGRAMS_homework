"""1. Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc). When the customer comes in, vendor asks "What do you want to buy?".
The customer can say "I want apple", or "Apple" or "three apple" or something like that. Your program will find out what fruit the customer is asking.  Your program will
also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc). Print the quantity if the customer says the quantity.
If not, ask him how much he wants."""
numbers_text = ["zero","one","two","three","four","five","six","seven","eight","nine"]
fruits = ["apple","orange","banana"]        #assigning intital variable to an array
quantity_apple , count_apple = 9 , 0        #set the default values of quantity and count
quantity_orange , count_orange = 9 , 0
quantity_banana , count_banana = 9 , 0
option = "y"
while (option == "y"):                      #while condition to check whether the user want to continue
    user_input = input("WHAT DO YOU WANT? (Apple,orange,banana) : ")
    user_input = user_input.lower()         #convert to lower case, so that it will be easy to check
    for temp_variable_num in numbers_text:  #using for loop run all numbers in char and check with user input
        if temp_variable_num  in user_input:
            if (quantity_apple > 0) and ("apple" in user_input or "apples" in user_input): #if apple present in user input
                count_apple += numbers_text.index(temp_variable_num)    
            if (quantity_orange > 0) and ("orange" in user_input or "oranges" in user_input): #if orange present in user input
                count_orange += numbers_text.index(temp_variable_num)
            if (quantity_banana > 0) and ("banana" in user_input or "bananas" in user_input): #if banana present in user input
                count_banana += numbers_text.index(temp_variable_num)
    if "quantity" in user_input:        #if customer ask for quantity
        print("APPLES BOUGHT  : ",count_apple)
        print("ORANGES BOUGHT : ",count_orange)
        print("BANANA BOUGHT  : ",count_banana)
    option = input("ENTER OPTION : ")

if (count_apple == 0) or (count_orange == 0) or (count_banana == 0): # if there is no count for any one of the fruit
    print("\n-PLEASE ENTER QUATITY, IF ENTERED ALREADY GIVE '0'-")
    count_apple += int(input("ENTER QUANTITY OF APPLE : "))
    count_orange += int(input("ENTER QUATITY OF ORANGES : "))
    count_banana += int(input("ENTER QUATITY OF BANANA : "))
quantity_apple -= count_apple
quantity_orange -= count_orange
quantity_banana -= count_banana
#to print the sales
print("\nAPPLES  SOLD : ",count_apple,", REMAINING : ",quantity_apple)
print("ORANGES SOLD : ",count_orange,", REMAINING : ",quantity_orange)
print("BANANAS SOLD : ",count_banana,", REMAINING : ",quantity_banana)
"""
---------- OUTPUT:1 ----------
WHAT DO YOU WANT? (Apple,orange,banana) : apple
ENTER OPTION : y
WHAT DO YOU WANT? (Apple,orange,banana) : two oranges
ENTER OPTION : y
WHAT DO YOU WANT? (Apple,orange,banana) : four bananas
ENTER OPTION : y
WHAT DO YOU WANT? (Apple,orange,banana) : quantity
APPLES BOUGHT  :  0
ORANGES BOUGHT :  2
BANANA BOUGHT  :  4
ENTER OPTION : n

-PLEASE ENTER QUATITY, IF ENTERED ALREADY GIVE '0'-
ENTER QUANTITY OF APPLE : 4
ENTER QUATITY OF ORANGES : 0
ENTER QUATITY OF BANANA : 0

APPLES  SOLD :  4 , REMAINING :  5
ORANGES SOLD :  2 , REMAINING :  7
BANANAS SOLD :  4 , REMAINING :  5
---------- OUTPUT:2 ----------
ENTER OPTION : y
WHAT DO YOU WANT? (Apple,orange,banana) : three bananas
ENTER OPTION : n

-PLEASE ENTER QUATITY, IF ENTERED ALREADY GIVE '0'-
ENTER QUANTITY OF APPLE : 0
ENTER QUATITY OF ORANGES : 0
ENTER QUATITY OF BANANA : 0

APPLES  SOLD :  2 , REMAINING :  7
ORANGES SOLD :  0 , REMAINING :  9
BANANAS SOLD :  3 , REMAINING :  6
"""