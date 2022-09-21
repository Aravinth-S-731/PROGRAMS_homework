"""Write a function that displays a square box with '*'. Input is the width of the sqaure."""
num = int(input("Enter the range : "))              #getting input from user
for i in range(0,num):                              #first for loop for rows
    for j in range(0,num):                          #second for loop for column
        #1st row , 1st column and last row and column
        if (j==0 or i==0 or i==num-1 or j==num-1):  #to print num if the condition satisfies
            print(num,end=" ")                      #to print the number
        else:
            print(" ",end=" ")                      #print space other than border row and column
    print()                                         #to print new line