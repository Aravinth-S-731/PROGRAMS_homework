alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtsuvwxyz"  #initial characters in a password
numbers = "0123456789"
special_char = "!@#$%^&*()_+-=[],.<>/?\|~`':;"
count_alpha , count_num , count_spec = 0 , 0 , 0
password = ""   #to store the password
while(len(password) < 8):   #to get password until therer is 8 or more letters
    password = input("ENTER YOUR PASSWORD WITH MINIMUM OF 8-CHARACTERS : ")
print("YOUR PASSWORD IS : ",password)
password_length = len(password)
if(password_length >= 8):   #only if the password length is greater or equal to 8, it shuld check the password
    for i in password:
        if(i in alphabets):     #for every alphabet increase the count of aphabet
            count_alpha += 1
        if(i in numbers):       #for every number increase the count of alphabet
            count_num += 1
        if(i in special_char):  #for every special character increase the count of special character
            count_spec +=1
if (password_length >= 16) and (count_alpha >= 3) and (count_num>= 2) and (count_spec >= 1):    #to check very strong pasword
    password_strength = "VERY STRONG"
elif (count_alpha >= 3) and (count_num>= 2) and (count_spec >= 1):  #to check strong password
    password_strength = "STRONG"
elif (count_alpha >= 1) and (count_num>= 1) and (count_spec >= 1):  #to check ok password
    password_strength = "OK"
else:                                                               #to check the weak password
    password_strength = "WEAK"
print(password,"is",password_strength)
"""
---------- OUTPUT:1 ----------
ENTER YOUR PASSWORD WITH MINIMUM OF 8-CHARACTERS : asdf
ENTER YOUR PASSWORD WITH MINIMUM OF 8-CHARACTERS : @aravinth@2002
YOUR PASSWORD IS :  @aravinth@2002
@aravinth@2002 is strong
---------- OUTPUT:2 ----------
ENTER YOUR PASSWORD WITH MINIMUM OF 8-CHARACTERS : aravinth
YOUR PASSWORD IS :  aravinth
aravinth is WEAK
"""