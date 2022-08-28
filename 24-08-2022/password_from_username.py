import random
""" Check if the username and password is correct."""
print("USERNAME SHOULD CONTAIN '@' and '.com' OR '.edu' OR '.org' OR '.tech' AT THE END")
#initial values
at_postion = 0
dot_position = 0
name_user = ""      #characters berfore '@'
company_name = ""   #characters in-between '@' and '.'
password = ""       #to store password
#getting username from user
username = input("ENTER YOU USERNAME : ")
username_length = len(username)

#to find postition of '@' and '.'
for i in range(0,username_length):
    if(username[i] == "@"):
        at_postion += i
    if(username[i] == "."):
        dot_position += i
#to store the characters befor '@' and in-between '@' and '.'
for i in range(0,at_postion):
    name_user += username[i]        #username before @
for i in range(at_postion+1,dot_position):
    company_name += username[i]     #company name after @ and before .
length_name_user , length_company_name = len(name_user) , len(company_name)
#to print the output
if(length_name_user >= 3) and (length_company_name != 0):  #output should be printed only if parameters follows
    #condition for declaring password with 1st , 3rd and last three letters befor @
    for i in range(0,length_name_user):
        if(i == 0) or  (i == 2) or (i == length_name_user-1) or (i == length_name_user-2) or (i == length_name_user-3):
            password += name_user[i]
    #condition for declaring password with first three letters after @ and before .
    for i in range(0,length_company_name):
        if(i == 0) or (i == 1) or (i == 2):
            password += company_name[i]
    #to print random 3 numbers
    for i in range(0,3):
        random_number = random.randint(0,9) #inbuilt function to print random numbers
        password += str(random_number)
    print("USERNAME : ",username)
    print("PASSWORD :",password)
else:
    if(at_postion == 0 or dot_position == 0):
        print("USERNAME MUST CONTAIN '@' AND A DOMAIN")
    elif(length_name_user < 3 and length_company_name < 1):
        print("NAME MUST CONSISTS OF THREE CHARACTERS and COMPANY NAME MUST NOT BE EMPTY eg: myname@companyname.domain")
    elif(length_name_user < 3):
        print("NAME MUST CONSISTS OF THREE CHARACTERS eg: myname@companyname.domain")
    elif(length_company_name < 1):
        print("COMPANY NAME MUST NOT BE EMPTY eg: myname@companyname.domain")
    else:
        None
"""
---------- OUTPUT:1 ----------
USERNAME SHOULD CONTAIN '@' and '.com' OR '.edu' OR '.org' OR '.tech' AT THE END
ENTER YOU USERNAME : ar@sethu.in 
NAME MUST CONSISTS OF THREE CHARACTERS eg: myname@companyname.domain
---------- OUTPUT:2 ----------
USERNAME SHOULD CONTAIN '@' and '.com' OR '.edu' OR '.org' OR '.tech' AT THE END
ENTER YOU USERNAME : aravinth@.com
COMPANY NAME MUST NOT BE EMPTY eg: myname@companyname.domain
---------- OUTPUT:3 ----------
USERNAME SHOULD CONTAIN '@' and '.com' OR '.edu' OR '.org' OR '.tech' AT THE END
ENTER YOU USERNAME : ar@.com
NAME MUST CONSISTS OF THREE CHARACTERS and COMPANY NAME MUST NOT BE EMPTY eg: myname@companyname.domain
---------- OUTPUT:4 ----------
USERNAME SHOULD CONTAIN '@' and '.com' OR '.edu' OR '.org' OR '.tech' AT THE END
ENTER YOU USERNAME : aravinthsethu.com
USERNAME MUST CONTAIN '@' AND A DOMAIN
---------- OUTPUT:5 ----------
ENTER YOU USERNAME : aravinth@sethu.in
USERNAME :  aravinth@sethu.in
PASSWORD : aanthset890
"""