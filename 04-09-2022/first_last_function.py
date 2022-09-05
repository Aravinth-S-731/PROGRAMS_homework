"""find the first A and last A, print all the letters between these two A.If there is no A or 2nd A is not found,
   find the first B  and last B and print all the letters between these two B.If there is no B or 2nd B is not found,
   find the first C and last C and print all the letters between these two C. Use functions."""

input_string = input("ENTER THE STRING : ") #getting input from user
length_input_string = len(input_string)     #length of string to run for loop
char = ""           #to store the character (A or B or C)
final_characters = []   #to store final charcters
index_of_a = []     #storing indexes of 'a'
index_of_b = []     #storing indexes of 'b'
index_of_c = []     #storing indexes of 'c'
starting_index = -1 #inital index
ending_index = -1   #intial index
errmsg = False      #to print error msg

def find_a(index_of_a): #to find 'a' in the string
    for index in range(0,length_input_string):
        if (input_string[index] == "a" or input_string[index] == "A"):
            index_of_a.append((index))
    return index_of_a
def find_b(index_of_b): #to find 'b' in the string
    for index in range(0,length_input_string):
        if (input_string[index] == "b" or input_string[index] == "B"):
            index_of_b.append((index))
    return index_of_b
def find_c(index_of_c): #to find 'c' in the string
    for index in range(0,length_input_string):
        if (input_string[index] == "c" or input_string[index] == "C"):
            index_of_c.append((index))
    return index_of_c
#to identify the starting index of charcters to printed
def find_start_end_index(final_characters ,starting_index ,ending_index ,errmsg ,char):
    if(len(index_of_a) >= 2):   #if two or more 'a' is present 
        char = "a"
        starting_index = index_of_a[0]
        ending_index = index_of_a[-1]
    elif(len(index_of_b) >= 2): #elif two or more 'b' is present
        char = "b"
        starting_index = index_of_b[0]
        ending_index = index_of_b[-1]
    elif(len(index_of_c) >= 2): #elif two or more 'c' is present
        char = "c"
        starting_index = index_of_c[0]
        ending_index = index_of_c[-1]
    else:                       #if one 'a,b,c' is missing or no 'a,b,c'
        errmsg = True
    if errmsg == False:         #if errmsg is false store the inbetween characters in a variable
        for index in range(starting_index+1,ending_index):
            final_characters += (input_string[index])
        print("THE CHARACTERS IN BETWEEN '",char,"' is : ",*final_characters)
    else:                       #else print the error message
        print("THERE IS ONLY ONE (or) NO A , B or C")
    return final_characters,starting_index,ending_index,errmsg,char

find_a(index_of_a)   #calling function to find 'a'
find_b(index_of_b)   #calling function to find 'b'
find_c(index_of_c)   #calling function to find 'c'
find_start_end_index(final_characters,starting_index,ending_index,errmsg,char)#calling to print output
"""
---------- OUTPUT:1 (a) ----------
ENTER THE STRING : asdfga
THE CHARACTERS IN BETWEEN ' a ' is :  s d f g
---------- OUTPUT:2 (b)----------
ENTER THE STRING : asdbcgdcb
THE CHARACTERS IN BETWEEN ' b ' is :  c g d c
---------- OUTPUT:2 (c)----------
ENTER THE STRING : casdfgcbdsfg
THE CHARACTERS IN BETWEEN ' c ' is :  a s d f g
---------- OUTPUT:2 (none)----------
ENTER THE STRING : asdfghjkl
THERE IS ONLY ONE (or) NO A , B or C
"""