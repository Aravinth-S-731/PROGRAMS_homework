from audioop import avg

#Intializing variable to store values
num = 1
sum = 0
count = 0

#While loop to get input from user 
while num != 0:
    #if num == 0:
    #   break
    num = int(input("Enter the number (or '0' to exit) : "))
    sum = sum + num

    #count += 1
    
    #if condition to count number of values entered
    if num != 0:
        count += 1

#to find average
average_value = sum / count

print("Number of values entered is",count,"and Sum of values is",sum)
print(average_value)