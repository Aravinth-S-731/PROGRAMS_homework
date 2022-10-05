import random                   #random function to choose random word
from termcolor import colored   #to print colored letters
Stored_words = []               #array to store the .txt file values
attempts_used = 1               #attempt used by user
attempts_limited = 7            #limit 
result = False                  #result whether th user found the word or not
user_word,current_output,check_output = None,None,"test"    #Defalut values

file = open('D:\Sayur\csv files\wordle.txt',mode='r')   #open the file
for row in file:                                        #for loop to run each and every row
    Stored_words.append(row.strip())                    #store the words in array without \n using strip
word_genarated = random.choice(Stored_words)            #genarate a random word to play

def get_word():                                         #getting input from user
    global attempts_used,user_word,result               #global variables
    while attempts_used < attempts_limited and result == False: #while attempts remain and result is False
        if check_output == user_word:                   #to check the word found is same as word genrated
            result = True                               #result is True
            break                                       #break the loop to get input
        user_word = input("Enter a 5-letter word (Attempt:"+str(attempts_used)+") : ")
        print("Your input is : ",user_word)
        attempts_used += 1                              #increment the attempt used
        check_word()                                    #call the function to check the word

def check_word():                                       #function to check the word
    global user_word,current_output,result,check_output #global variables
    index = 0                                           #starting index is 0
    current_output,check_output = "" , ""               #output before checking
    for char in user_word:                              #for loop to run every letter
        if char == word_genarated[index]:               #if the letter is in correct index
            current_output += colored(char,"green")     #turn green
            check_output += char                        #concatinate the letter to check
        elif char in word_genarated:                    #if the letter is in the word but wrong index
            current_output += colored(char,"yellow")    #turn yellow
        else:                               
            current_output += colored(char,"red")       #else red
        index += 1                                      #increment the index to check next letter
    print("MATCHED LETTERS : ",current_output)          #print the result of the current input word

get_word()                                              #call the get_word function
if result == False:                                     #if attempts are over
    print("SORRY! YOU USED ALL YOUR ATTEMPTS. THE WORD IS :",word_genarated)
else:                                                   #if user found the word
    print("YOU WON!. NUMBER OF ATTEMPTS:",attempts_used-1)
"""
---------- OUTPUT:1 ----------
Enter a 5-letter word (Attempt:1) : happy
Your input is :  happy
MATCHED LETTERS :  happy
Enter a 5-letter word (Attempt:2) : truck
Your input is :  truck
MATCHED LETTERS :  truck
Enter a 5-letter word (Attempt:3) : lucky
Your input is :  lucky
MATCHED LETTERS :  lucky
Enter a 5-letter word (Attempt:4) : clock
Your input is :  clock
MATCHED LETTERS :  clock
Enter a 5-letter word (Attempt:5) : cycle
Your input is :  cycle
MATCHED LETTERS :  cycle
Enter a 5-letter word (Attempt:6) : hello
Your input is :  hello
MATCHED LETTERS :  hello
SORRY! YOU USED ALL YOUR ATTEMPTS. THE WORD IS : excel
---------- OUTPUT:2 ----------
Enter a 5-letter word (Attempt:1) : happy
Your input is :  happy
MATCHED LETTERS :  happy
Enter a 5-letter word (Attempt:2) : holes
Your input is :  holes
MATCHED LETTERS :  holes
Enter a 5-letter word (Attempt:3) : clock
Your input is :  clock
MATCHED LETTERS :  clock
Enter a 5-letter word (Attempt:4) : cloth
Your input is :  cloth
MATCHED LETTERS :  cloth
YOU WON!. NUMBER OF ATTEMPTS: 4
"""