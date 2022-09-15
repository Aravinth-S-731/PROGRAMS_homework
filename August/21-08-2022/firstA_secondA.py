#to get string from user
input_string = input("ENTER A STRING WITH ONLY TWO A's : ")
input_string = list(input_string)               #converting string into array
len_input = len(input_string)
print("THE ENTERED STRING IS : ",input_string)
output_string = []
err_msg = True
index_of_a = [] #to store the index were the character 'a' is located

#search for 'a'
for i in range(0,len_input):
    if(input_string[i] == "a" or input_string[i] == "A"):
        index_of_a.append(i)    #storing indexes of 'a'
index_a_length = len(index_of_a)
#to print the character in between first and second 'a'
if(index_a_length >= 2):
    err_msg = False
    start = index_of_a[0]
    end = index_of_a[1]
    for i in range(start+1,end):    #start+1 to stop first'a' from printing
        output_string.append(input_string[i])
    print(*output_string)
else:
    print("THERE IS ONLY ONE 'a' OR NO 'a'")
"""
---------- OUTPUT:1 -----------
ENTER A STRING WITH ONLY TWO A's : apple    
THE ENTERED STRING IS :  ['a', 'p', 'p', 'l', 'e']
THERE IS ONLY ONE 'a' OR NO 'a'
---------- OUTPUT:2 -----------
ENTER A STRING WITH ONLY TWO A's : alphabeta
THE ENTERED STRING IS :  ['a', 'l', 'p', 'h', 'a', 'b', 'e', 't', 'a']
l p h
"""