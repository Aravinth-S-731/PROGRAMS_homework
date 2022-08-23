#getting string as input and converting to array
string1 = input("ENTER THE STRING-1 : ")
string2 = input("ENTER THE STRING-2 : ")
string1 = list(string1) #Input given is taken as string, whereas we need each and induvidual character so it is converted into list
string2 = list(string2) #Input given is taken as string, whereas we need each and induvidual character so it is converted into list
string1_length = len(string1)
string2_length = len(string2)
same_char_in_two_strings = [] #to store same charactres in two strings
after_removing_duplicate = [] #to remove duplicates from repeated characters

#for loop to fing same characters
for i in range(0,string1_length):
    for j in range(0,string2_length):
        if(string1[i] == string2[j]):
            temp_var = string1[i]
            same_char_in_two_strings.append(temp_var)

#for loop to remove duplicate from the repeated character array
for i in same_char_in_two_strings:
    if i not in after_removing_duplicate:
        after_removing_duplicate.append(i)

print("\nTHE CHARACTERS IN BOTH STRINGS ARE : ",after_removing_duplicate)

#---------- OUTPUT ----------
# ENTER THE STRING-1 : aravinth
# ENTER THE STRING-2 : arvind

# THE CHARACTERS IN BOTH STRINGS ARE :  ['a', 'r', 'v', 'i', 'n']