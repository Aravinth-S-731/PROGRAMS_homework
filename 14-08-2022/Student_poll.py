#Assigning variables with initial values
no_of_stud = 10
f_online , f_offline , f_mixed = 0 , 0 , 0
m_online , m_offline , m_mixed = 0 , 0 , 0
option = None

#for loop to run according to number of students
for i in range(0,no_of_stud):

    #if condition to break if user choose to end "no comment"
    if option == "no comment":   
        break

    #else condition to get gender and the option
    else:
        gender = input("ENTER GENDER (male / female) : ")
        if gender == "female":
            print("1.ONLINE\n2.OFFLINE\n3.MIXED\n4.no comment")
            option = input("Enter the option ('no comment' to end) : ")
            if option == "1":
                f_online += 1
            elif option == "2":
                f_offline += 1
            elif option == "3":
                f_mixed += 1
            else:
                None
        elif gender == "male":
            print("1.ONLINE\n2.OFFLINE\n3.MIXED\n4.no comment")
            option = input("Enter the option ('no comment' to end) : ")
            if option == "1":
                m_online += 1
            elif option == "2":
                m_offline += 1
            elif option == "3":
                m_mixed += 1
            else:
                None
        else:
            print("Enter valid gender")
    print("\n")

#to print option choosen by students according to gender
print("ONLINE  CLASS  FEMALE :",f_online,", MALE :",m_online)
print("OFFLINE CLASS  FEMALE :",f_offline,", MALE :",m_offline)
print("MIXED   CLASS  FEMALE :",f_mixed,", MALE :",m_mixed)

#percentage of students that like online classes
total_registration = f_online + f_offline + f_mixed + m_online + m_offline + m_mixed
female_online_percentage = (f_online / total_registration) * 100
print("\n PERCENTAGE OF FEMALE STUDENTS INTRESTED IN ONLINE CLASS IS : ",female_online_percentage,"%")