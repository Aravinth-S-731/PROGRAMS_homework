input_string1 = input("ENTER THE STRING1 : ")     #getting input from user
input_string2 = input("ENTER THE STRING2 : ")
output_string = ""
string_length1 = len(input_string1)
string_length2 = len(input_string2)
max_string_length = max(string_length1,string_length2) #finding the maximun of both string length to run the for loop
for index in range(0,max_string_length):
    if index <= string_length1-1:
        output_string += input_string1[index]       #to store the character in first string
    if index <= string_length2-1:
        output_string += input_string2[index]       #to store the character in second string
print(output_string)
"""
---------- OUTPUT:1 (equal no of char in both strings)----------
ENTER THE STRING1 : AAAAA
ENTER THE STRING2 : SSSSS
ASASASASAS
---------- OUTPUT:2 (different no of char in both strings)----------
ENTER THE STRING1 : ABCD
ENTER THE STRING2 : 12345
A1B2C3D45
"""