#inital values
no_of_phones = []
emp_salary = 10000
commision = 1000
#phones_5 = (commision + 100) * 5
#phones_10 = (commision + 200)*10 - (phones_5)
commision_by_selling_phones = []
total_salary = []
yearly_salary = 0
max_emp_salary = 25000

#Number of phone for 12 months
for i in range(0,12):
    print("ENTER THE MOBILE PHONE SOLD ON MONTH",i+1,": ")
    temp_var = int(input())
    no_of_phones.append(temp_var)

#calculate salary per month
for i in range(0,12):

    #when the quantity is less than five commision for each phone is 1000/-
    if no_of_phones[i] < 5:
        less_than_5 = no_of_phones[i] * commision
        commision_by_selling_phones.append(less_than_5)

    #when the quatity is >= 5 and < 10 the commision is 1000+100 each phone
    elif no_of_phones[i] >= 5 and no_of_phones[i] < 10:
        less_than_10 = (commision + 100) * no_of_phones[i]
        commision_by_selling_phones.append(less_than_10)

    #when the quatity is >= 10 the commision is 1000+200 each phone apart from the first 5 phones
    elif no_of_phones[i] >= 10:
        greater_than_10 = ((commision + 200) * (no_of_phones[i]-5)) + ((commision + 100) * 5)
        commision_by_selling_phones.append(greater_than_10)

    #calculate total salary for each months including commision = 1000/-
    per_month_sal = emp_salary + commision_by_selling_phones[i]
    total_salary.append(per_month_sal)

    #total salary for a year
    yearly_salary = yearly_salary + total_salary[i]

#to print each mont salary
for i in range(0,12):
    print("MONTHLY SALARY OF MONTH",i+1,"IS : ",total_salary[i])

#annual income of employee and average income per month in a year
avg_sal = yearly_salary / 12
print("\nTHE ANNUAL INCOME IS : ",yearly_salary)
print("AVERAGE MONTHLY INCOME PER YEAR IS : ",round(avg_sal))