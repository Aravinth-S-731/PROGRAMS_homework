fruits = ["apple","orange","banana"]                            #fruit list
num_char = ["zero","one","two","three","four","five","six","seven","eight","nine"]  #numbers in characters
length = len(fruits)                                            #length of fruit
user_input = None                                               #user input is None in initial
limit_quantity = [9,9,9]                                        #limit of sales
count_friuits = [0,0,0]                                         #count of fruits sold
option = "y"                                                    #whether user want to continue   
    
def customerinput():                                            #function to get input from user
    global user_input                                           #global variable to use it in other funtions
    user_input = input("WHAT DO YOU WANT : ")                   
    for index_fruit in range(0,length):                         #for loop to run the values 
        if (count_friuits[index_fruit]  >= 9):                  #if count of a fruit is greater than or equal to break the loop
            break
        if((fruits[index_fruit]) in user_input):                #to check if the user_input contains the fruit
            for index_num in range(0,10):                       #for loop to run all numbers in characters
                if(num_char[index_num] in user_input):          #if the numbers in characters in user_input add the value to the count_fruits
                    count_friuits[index_fruit] += index_num
            if(count_friuits[index_fruit] == 0):                #if the count is not given in the user_input ask user for count
                count_friuits[index_fruit] += int(input("ENTER COUNT OF "+fruits[index_fruit]+": "))

while (option == "y"):                                          #whetjer the user want to continue
    for index in range(0,length):                               #to check the stock of fruits
        if (limit_quantity[index] <= count_friuits[index]):
            print(fruits[index]+" IS OUT OF STOCK")
    customerinput()                                             #calling the customerinput() funtion
    option = input("CONTINUE (y/n) : ")                         #user input to continue or to end
for index in range(0,length):
    print(fruits[index]+" SOLD IS : ",count_friuits[index])
"""
---------- OUTPUT:1 ----------
WHAT DO YOU WANT : one apple
CONTINUE (y/n) : y
WHAT DO YOU WANT : orange
ENTER COUNT OF orange: 5
CONTINUE (y/n) : y
WHAT DO YOU WANT : three banana
CONTINUE (y/n) : n
apple SOLD IS :  1
orange SOLD IS :  5
banana SOLD IS :  3
---------- OUTPUT:2 ----------
WHAT DO YOU WANT : three orange
CONTINUE (y/n) : y
WHAT DO YOU WANT : banana
ENTER COUNT OF banana: 9
CONTINUE (y/n) : y
banana IS OUT OF STOCK
WHAT DO YOU WANT : apple
ENTER COUNT OF apple: 9
CONTINUE (y/n) : y
apple IS OUT OF STOCK
banana IS OUT OF STOCK
WHAT DO YOU WANT : two apple
CONTINUE (y/n) : n
apple SOLD IS :  9
orange SOLD IS :  3
banana SOLD IS :  9
"""