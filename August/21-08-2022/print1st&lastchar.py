input_string = input("ENTER THE STRING : ")     #getting input from user
output_string =""
string_length = len(input_string)
break_point = string_length / 2     #to find the value to break the loop
if string_length % 2 == 0:
    for index in range(0,string_length):
        output_string += str(input_string[index])
        output_string += str(input_string[string_length-index-1])
        output_string += (",")
        if index == break_point-1:  #if condition to break the loop after running half the string length
            break
    print(output_string)
else:
    print("PLEASE ENTER AN EVEN COUNT OF STRING")
""" 
---------- OUTPUT:1 ----------
ENTER THE STRING : asdfg12345
a5,s4,d3,f2,g1,
---------- OUTPUT:2 ----------
ENTER THE STRING : asdfg1234
PLEASE ENTER AN EVEN COUNT OF STRING 
"""