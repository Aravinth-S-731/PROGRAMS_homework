"""1. Write an app to calculate Grades for students in each subject.Mark > 90 is A, > 80 is B, > 70 is C, > 60 is D. 
anything less than 60 is fail.Write a function that returns the grade for one subject for all the students in the class.Also,
 print the class avg grade."""
student_count = 0               # to check how many students marks are collected
#USING MULTI-DIMENSIONAL ARRAY
marks = [[],[],[],[],[]]        #total subjects is - 5
student_option = "y"            #whether user want to countinue to enter STUDENT MARKS
subject_option = "y"            #whether user want to check grade for another subject

def get_marks():                #getting marks from user
    global student_count 
    student_count += 1          #student count
    print("----MARK FOR STUDENT",student_count,"----")
    for index in range(0,5):
        temp_var = int(input("ENTER MARK OF SUBJECT "+str(index+1)+" : "))
        marks[index].append(temp_var)

def subject_grade():            #to check student grade for the given subject
    for index in range(0,len(marks[check_subject-1])):  #len(marks[check_subject-1])-is given to find total students in one subject
        if marks[check_subject-1][index] > 90:  #if >90 'A' grade
            print("STUDENT",index+1,"GOT 'A' GRADE IN SUBJECT",check_subject)
        elif marks[check_subject-1][index] > 80:#if >90 'B' grade
            print("STUDENT",index+1,"GOT 'B' GRADE IN SUBJECT",check_subject)
        elif marks[check_subject-1][index] > 70:#if >70 'c' grade
            print("STUDENT",index+1,"GOT 'C' GRADE IN SUBJECT",check_subject)
        elif marks[check_subject-1][index] > 60:#if >60 'D' grade
            print("STUDENT",index+1,"GOT 'D' GRADE IN SUBJECT",check_subject)
        else:                                   #>= 60 fail 
            print("STUDENT",index+1,"IS FAIL IN SUBJECT",check_subject)

while student_option == "y":    #whether user want to countiue entering student details
    get_marks()                 #calling get_marks() function
    student_option = input("DO U WNAT TO GET MARK OF ANOTHER STUDENT (y/n): ")

while subject_option == "y":    #whether user want to check another subject amrk
    check_subject = (int(input("ENTER SUBJECT TO CHECK(1,2,3,4,5) : ")))
    subject_grade()             #calling subject_grade() function
    subject_option = input("DO U WANT TO CHECK ANOTHER SUBJECT (y/n): ")

"""
---------- OUTPUT ----------
----MARK FOR STUDENT 1 ----
ENTER MARK OF SUBJECT 1 : 100
ENTER MARK OF SUBJECT 2 : 90
ENTER MARK OF SUBJECT 3 : 80
ENTER MARK OF SUBJECT 4 : 70
ENTER MARK OF SUBJECT 5 : 60
DO U WNAT TO GET MARK OF ANOTHER STUDENT (y/n): y
----MARK FOR STUDENT 2 ----
ENTER MARK OF SUBJECT 1 : 60
ENTER MARK OF SUBJECT 2 : 70
ENTER MARK OF SUBJECT 3 : 80
ENTER MARK OF SUBJECT 4 : 9
ENTER MARK OF SUBJECT 5 : 99
DO U WNAT TO GET MARK OF ANOTHER STUDENT (y/n): y
----MARK FOR STUDENT 3 ----
ENTER MARK OF SUBJECT 1 : 44
ENTER MARK OF SUBJECT 2 : 55
ENTER MARK OF SUBJECT 3 : 66
ENTER MARK OF SUBJECT 4 : 56
ENTER MARK OF SUBJECT 5 : 65
DO U WNAT TO GET MARK OF ANOTHER STUDENT (y/n): n
ENTER SUBJECT TO CHECK(1,2,3,4,5) : 1
STUDENT 1 GOT 'A' GRADE IN SUBJECT 1
STUDENT 2 IS FAIL IN SUBJECT 1
STUDENT 3 IS FAIL IN SUBJECT 1
DO U WANT TO CHECK ANOTHER SUBJECT (y/n): y
ENTER SUBJECT TO CHECK(1,2,3,4,5) : 2
STUDENT 1 GOT 'B' GRADE IN SUBJECT 2
STUDENT 2 GOT 'D' GRADE IN SUBJECT 2
STUDENT 3 IS FAIL IN SUBJECT 2
DO U WANT TO CHECK ANOTHER SUBJECT (y/n): y
ENTER SUBJECT TO CHECK(1,2,3,4,5) : 3
STUDENT 1 GOT 'C' GRADE IN SUBJECT 3
STUDENT 2 GOT 'C' GRADE IN SUBJECT 3
STUDENT 3 GOT 'D' GRADE IN SUBJECT 3
DO U WANT TO CHECK ANOTHER SUBJECT (y/n): y
ENTER SUBJECT TO CHECK(1,2,3,4,5) : 4
STUDENT 1 GOT 'D' GRADE IN SUBJECT 4
STUDENT 2 IS FAIL IN SUBJECT 4
STUDENT 3 IS FAIL IN SUBJECT 4
DO U WANT TO CHECK ANOTHER SUBJECT (y/n): y
ENTER SUBJECT TO CHECK(1,2,3,4,5) : 5
STUDENT 1 IS FAIL IN SUBJECT 5
STUDENT 2 GOT 'A' GRADE IN SUBJECT 5
STUDENT 3 GOT 'D' GRADE IN SUBJECT 5
DO U WANT TO CHECK ANOTHER SUBJECT (y/n): n
"""