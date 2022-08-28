alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtsuvwxyz"
numbers = "0123456789"
special_char = "!@#$%^&*()_+-=[],.<>/?\|~`':;"
count_alpha , count_num , count_spec = 0 , 0 , 0
password = ""
while(len(password) < 8):
    password = input("ENTER YOUR PASSWORD WITH MINIMUM OF 8-CHARACTERS : ")
print(password)
password_length = len(password)
if(password_length >= 8):
    for i in password:
        if(i in alphabets):
            count_alpha += 1
        if(i in numbers):
            count_num += 1
        if(i in special_char):
            count_spec +=1
if (password_length >= 16) and (count_alpha >= 3) and (count_num>= 2) and (count_spec >= 1):
    password_strength = "VERY STRONG"
elif (count_alpha >= 3) and (count_num>= 2) and (count_spec >= 1):
    password_strength = "STRONG"
elif (count_alpha >= 1) and (count_num>= 1) and (count_spec >= 1):
    password_strength = "OK"
elif (count_alpha == password_length) or (count_num == password_length) or (count_spec == password_length):
    password_strength = "WEAK"
print(password_strength)