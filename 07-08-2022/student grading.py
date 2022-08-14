#getting student marks
from webbrowser import Elinks


mark = []
for i in range(0,5):
    a = int(input("ENTER THE MARK FOR : "))
    mark.append(a)

#overall percentage
sum = 0
for j in range(0,5):
    sum += mark[j]      #sum of all marks
tot_percentage = sum / 5
print("THE OVERALL PERCENTAGE IS : ",tot_percentage)

#count number of subjects above 90% and nuber of subjects above 40%
above_90 = 0
above_40 = 0
for k in range(0,5):
    if(mark[k] >= 90):
        above_90 += 1
    elif(mark[k] >= 40):
        above_40 += 1
    else:
        None

#count number of subjects above 75% and nuber of subjects above 50%
above_75 = 0
above_50 = 0
for k in range(0,5):
    if(mark[k] >= 75):
        above_90 += 1
    elif(mark[k] >= 50):
        above_40 += 1
    else:
        None

#pass or fail
if(tot_percentage >= 60):
    print("PASS")
elif(above_90 >= 3 & above_40>= 2):
    print("pass")
elif(above_75 >= 3 & above_50 >= 2):
    print("PASS")
else:
    print("FAIL")
