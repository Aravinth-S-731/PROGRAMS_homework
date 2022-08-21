#Initial variables
student_name = []
student_mark = []
total_mark = 0
student_count = 0
option = "y"


for i in range (0,student_count+1): # +1 for considering the last value
    while(option == "y"):
        student_count += 1      #to count no of studnets  
        temp_var = input("\nENTER THE "+ str(student_count) +" STUDENT NAME : ")
        student_name.append(temp_var)
        option = input("DO YOU WANT TO CONTINUE (y/n) : ")
        
reverse_student_name = student_name[::-1]       #to reverse the array content

#for loop to get mark
for i in range(0,student_count): 
    temp_var = int(input("ENTER THE MARK OF "+ str(reverse_student_name[i]) +" : "))
    student_mark.append(temp_var)
    total_mark += student_mark[i]

#for loop to print the marks
for i in range(0,student_count):
    print(student_name[i]," SCORED : ",student_mark[i])

avg_mark = total_mark / student_count
print("THE CLASS AVERAGE IS : ",avg_mark)

# ---------- OUTPUT ----------
# ENTER THE 1 STUDENT NAME : ARAVINTH
# DO YOU WANT TO CONTINUE (y/n) : y

# ENTER THE 2 STUDENT NAME : NANDHA
# DO YOU WANT TO CONTINUE (y/n) : y

# ENTER THE 3 STUDENT NAME : NIRMAL
# DO YOU WANT TO CONTINUE (y/n) : y

# ENTER THE 4 STUDENT NAME : RAVI
# DO YOU WANT TO CONTINUE (y/n) : n
# ENTER THE MARK OF RAVI : 99
# ENTER THE MARK OF NIRMAL : 88
# ENTER THE MARK OF NANDHA : 77
# ENTER THE MARK OF ARAVINTH : 66
# ARAVINTH  SCORED :  99
# NANDHA  SCORED :  88
# NIRMAL  SCORED :  77
# RAVI  SCORED :  66
# THE CLASS AVERAGE IS :  82.5