"""write a function that generates a random number that is always divisible by the input number. 
For eg, if input is 5, the randome number function should only generate numbers 5,20, 15, 75, etc."""
import random                                       #random package
x = int(input("ENTER THE NUMBER : "))                       #getting input from user
start = x                                           #start of range
end = x*x                                           #end of range

def divisible_by_input(num1,num2,div_num):          #defining fuction to find the value
    num_div_by_input = random.randint(num1, num2)   #genarate a radom number to check
    while num_div_by_input % div_num != 0:          #if the reminder is not '0'
      num_div_by_input = random.randint(num1, num2) #genarate a another random number
    return num_div_by_input                         #return the value

print(divisible_by_input(start,end,x))              #print the output by calling the function
"""
---------- OUTPUT:1 ----------
ENTER THE NUMBER : 765
210375
---------- OUTPUT:2 ----------
ENTER THE NUMBER : 7
28
---------- OUTPUT:3 ----------
ENTER THE NUMBER : 7865
14526655
---------- OUTPUT:4 ----------
ENTER THE NUMBER : 1111
334411
"""