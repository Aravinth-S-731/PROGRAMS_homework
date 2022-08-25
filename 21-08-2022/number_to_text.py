from pickle import FALSE
from tkinter import TRUE

#initialize values
numbers = ["0","1","2","3","4","5","6","7","8","9"]
characters = ["ZERO ","ONE ","TWO ","THREE ","FOUR ","FIVE ","SIX ","SEVEN ","EIGHT ","NINE "]
output_characters = ""
err_msg = TRUE

#get input from user
user_input = input("ENTER THE NUMBER TO BE CONVERTED INTO TEXT : ")
user_input = list(user_input)
user_input_length = len(user_input) #used for running 'for' loop

#for loop to print the text to respective numbers
for i in range(0,10): #hardcode because no change in length
    #for i in range(0,user_input_length):
    for j in range(0,user_input_length):
        if numbers[i] == user_input[j]:
            output_characters += characters[i]
            err_msg = FALSE

print(output_characters)
if err_msg == TRUE:
    print("PLEASE ENTER A VALID INPUT")

""" ---------- OUTPUT:1 ----------
ENTER THE NUMBER TO BE CONVERTED INTO TEXT : 123
ONE TWO THREE 
    ---------- OUTPUT:2 ----------
ENTER THE NUMBER TO BE CONVERTED INTO TEXT : asd
PLEASE ENTER A VALID INPUT"""