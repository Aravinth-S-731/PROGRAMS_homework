mark = []
for i in range(0,5):
    a = int(input("ENTER THE MARK FOR : "))
    mark.append(a)

#count number of subjects above 90% and nuber of subjects above 40%
#count number of subjects above 75% and nuber of subjects above 50%
above_90 = 0
above_75 = 0
above_60 = 0
above_50 = 0
above_40 = 0
below_40 = 0
for k in range(0,5):
    if(mark[k] > 60):
        above_60 +=1
    if(mark[k] >= 90):
        above_90 += 1
    elif(mark[k] >= 75):
        above_75 += 1
    elif(mark[k] >= 50):
        above_50 += 1
    elif(mark[k] >= 40):
        above_40 += 1
    else:
        below_40 += 1


#pass or fail
if(above_60 == 5):
    print("PASS")
elif(above_90 >= 3):
    if(above_40 >=2 | above_40 >=1):
            print("pass")
elif(above_75 >= 3):
    if(above_50 >= 2 | above_50 >= 1):
            print("PASS")
else:
    print("FAIL")