input_string = input("ENTER THE STRING : ")     #getting input from user
string_length = len(input_string)
even_index_char = ""                #empty varibles for storing values 
even_reverse_index_char = ""
odd_index_char = ""
for index in range(0, string_length):   #for loop to find odd and even indexed values
    if index % 2 == 0:
        even_index_char += input_string[index]  #storing even indexd value
    else:
        odd_index_char += input_string[index]   #storing odd index values
for index in range(len(even_index_char)-1,-1,-1):   #for loop for reversing even indexed characters
    even_reverse_index_char += even_index_char[index]
print("ODD INDEX CHARACTERS : ",odd_index_char)
print("REVERSED EVEN INDEXED CHARATCERS : ",even_reverse_index_char)
"""
---------- OUTPUT:1 ----------
ENTER THE STRING : aravinth
ODD INDEX CHARACTERS :  rvnh
REVERSED EVEN INDEXED CHARATCERS :  tiaa
---------- OUTPUT:2 ----------
ENTER THE STRING : asddfghj12345
ODD INDEX CHARACTERS :  sdgj24
REVERSED EVEN INDEXED CHARATCERS :  531hfda
"""