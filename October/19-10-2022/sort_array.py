array_elements = [5,16,1,4,7]                                   #declaring random array
print("THE UNSORTED ARRAY : ",*array_elements)                   #print the original array
temp_var = []                                                   #temp var to store the value

for index1 in range(0,len(array_elements)):                     #first for loop to check from 0th index
    for index2 in range( (index1 + 1) , len(array_elements) ):  #second for loop to check the oth index to other index
        if  array_elements[index2] < array_elements[index1]:    #if the compared values in the index is greater
            temp_var = array_elements[index1]                   #store the value in temp var
            array_elements[index1] = array_elements[index2]     #swap the values
            array_elements[index2] = temp_var
    print(array_elements)                                       #change of each and every number
print("THE SORTED ARRAY : ",array_elements)                     #print sorted array