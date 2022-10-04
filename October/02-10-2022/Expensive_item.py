import csv
content = []    #to store the csv values
index = 1       #index of the content
price = -1      #price of the costliest item

file = open("D:\Sayur\cafe.csv",mode="r")   #opening the item
csvreading = csv.reader(file)               #opening as reader object
for row in csvreading:                      #loop to store content in csv as array elements
    content.append(row)
size = len(content)
for i in range(1,size): 
    check_val = int(content[index][1])      #storing the price values in temporary variable
    index += 1                              #incrementing the index
    if price < check_val:                   #check for the maximum value
        price = check_val                   #if true store the max value
        row_of_item = i                     #record the row in which max value is found
print("THE ITEM WHICH IS EXPENSIVE IS : ",content[row_of_item][0],"  WITH PRICE : ",price)

"""
---------- OUTPUT ----------
THE ITEM WHICH IS EXPENSIVE IS :  Pizza   WITH PRICE :  200
"""