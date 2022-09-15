#to get string from user
input_string = input("ENTER A STRING WITH ONLY TWO A's : ")
input_string = list(input_string)               #converting string into array
len_input = len(input_string)
print("THE ENTERED STRING IS : ",input_string)
output_string = []
err_msg = True
index_of_a = [] #to store the index were the character 'a' is located
index_of_n = [] #to store the index were the character 'n' is located

#search for 'a' and 'n'
for i in range(0,len_input):
    if(input_string[i] == "a" or input_string[i] == "A"):
        index_of_a.append(i)    #storing indexes of 'a'
    elif(input_string[i] == "n" or input_string[i] == "N"):
        index_of_n.append(i)    #storing indexes of 'n'
index_length_a = len(index_of_a)
index_length_n = len(index_of_n)

#to print the values between start and end of 'a'
if(index_length_a >=1 and index_length_n >= 1):
    err_msg = False
    #start and end index of 'a'
    start = index_of_a[0]
    end = index_of_n[-1]
    print("\nTHE VALUES BETWEEN TWO 'a' ARE")
    for i in range(start+1,end):    #start+1 to stop 'a' from printing
        output_string.append(input_string[i])
if(err_msg == True):
    print("\nTHERE IN ONLY ONE 'a' OR ONE 'n' / OR THERE IS NO 'a' OR 'n'")
else:
    print(*output_string)
"""
---------- OUTPUT:1 -----------
ENTER A STRING WITH ONLY TWO A's : Aravinth
THE ENTERED STRING IS :  ['A', 'r', 'a', 'v', 'i', 'n', 't', 'h']

THE VALUES BETWEEN TWO 'a' ARE
r a v i
---------- OUTPUT:2 -----------
ENTER A STRING WITH ONLY TWO A's : apple
THE ENTERED STRING IS :  ['a', 'p', 'p', 'l', 'e']

THERE IN ONLY ONE 'a' OR ONE 'n' / OR THERE IS NO 'a' OR 'n'
"""