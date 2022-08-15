no_of_stud = 3  #number of students
no_of_subj = 3  #number of subjects
stud1_mark = [] #array for marks
stud2_mark = []
stud3_mark = []
stud1_gpa = 0   #intial variable for gpa calculation
stud2_gpa = 0
stud3_gpa = 0

#loop to get input from user
for i in range(0,no_of_stud):
    for j in range(0,no_of_subj):
        print("Enter the mark for student",i+1,": subject-",j+1)
        temp_variable = int(input())
        if(i == 0):
            stud1_mark.append(temp_variable)
        if(i == 1):
            stud2_mark.append(temp_variable)
        if(i == 2):
            stud3_mark.append(temp_variable)

#loop to display the enterd mark
for i in range(0,no_of_stud):
    for j in range (0,no_of_subj):
        if(i == 0):
            print("The mark obtained by student",i+1,"in subject",j,"is",stud1_mark[i])
            stud1_gpa += stud1_mark[i]
        if(i == 1):
            print("The mark obtained by student",i+1,"in subject",j,"is",stud2_mark[i])
            stud2_gpa += stud2_mark[i]
        if(i == 2):
            print("The mark obtained by student",i+1,"in subject",j,"is",stud3_mark[i])
            stud3_gpa += stud3_mark[i]
print("\n")
#to calculate GPA
stud1_gpa = (stud1_gpa / no_of_subj) 
stud2_gpa = (stud2_gpa / no_of_subj) 
stud3_gpa = (stud3_gpa / no_of_subj) 
print("GPA of Student 1: ",stud1_gpa / 10)
print("GPA of Student 2: ",stud2_gpa / 10)
print("GPA of Student 3: ",stud3_gpa / 10)
#class average mark
class_average = (stud1_gpa + stud2_gpa + stud3_gpa) / no_of_stud
print("THE CLASS AVERAGE IS : ",class_average)