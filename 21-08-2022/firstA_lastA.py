#to get string from user
input_string = input("ENTER A STRING WITH ONLY TWO A's : ")
input_string = list(input_string)
len_input = len(input_string)
print("THE ENTERED STRING IS : ",input_string)

index_of_a = [] #to store the index were the character 'a' is located

#search for 'a'
for i in range(0,len_input):
    if(input_string[i] == "a"):
        temp_var = i
        index_of_a.append(temp_var)
index_length = len(index_of_a)
#to print the values between start and end of 'a'
if(index_length >= 2):
    #start and end index of 'a'
    start = index_of_a[0]
    end = index_of_a[-1]
    print("\nTHE VALUES BETWEEN TWO 'a' ARE")
    for i in range(start+1,end):
        print(input_string[i])
else:
    print("\nTHERE IN ONLY ONE 'a' OR NO 'a' IN THE GIVEN STRING")

#---------- OUTPUT:1 ----------
# THE ENTERED STRING IS :  ['s', 'd', 'f', 'a', 'w', 'e', 'r', 't', 's', 'a', 's', 'j', 'k', 'a', 's', 'd']

# THE VALUES BETWEEN TWO 'a' ARE
# w
# e
# r
# t
# s
# a
# s
# j
# k
# -------- OUTPUT:2 ----------
# THE ENTERED STRING IS :  ['d', 'f', 'n', 'l', 'f', 's', 'g', 'n', 'o', 'l', 'd', 'f', 'v']

# THERE IN ONLY ONE 'a' OR NO 'a' IN THE GIVEN STRING