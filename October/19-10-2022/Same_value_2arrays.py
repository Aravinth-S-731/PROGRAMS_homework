array1 = [1,3,7,9,13,14]                        #array 1
array2 = [1,2,5,7,13,15]                        #array 2
same_val = []                                   #array to store same values in both array

for arr1 in range(len(array1)):                 #for loop to check each values in array 1
    for arr2 in range(len(array2)):             #for loop to check each values in array 2
        if (array1[arr1] == array2[arr2]):      #if thr both values are same
            same_val.append(array1[arr1])       #store the values in same_value[] array
print("ARRAY-1 : ",array1)
print("ARRAY-2 : ",array2)
if not same_val:
    print("NO SAME VALUES")
else:
    print("SAME VALUES IN BOTH ARRAY : ",same_val)

"""
---------- OUTPUT:1 ----------
ARRAY-1 :  [1, 3, 7, 9, 13, 14]
ARRAY-2 :  [1, 2, 5, 7, 13, 15]
SAME VALUES IN BOTH ARRAY :  [1, 7, 13]
---------- OUTPUT:2 ----------
ARRAY-1 :  [1, 2, 3, 4]
ARRAY-2 :  [5, 6, 7, 8]
NO SAME VALUES
"""