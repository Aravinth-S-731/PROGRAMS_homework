#cost of lunch per person
lunch = int(input("ENTER THE COST OF LUNCH PER PERSON : "))
count = int(input("ENTER TOTAL NUMBER OF GUESTS : "))
print("COST OF LUNCH PER PERSON IS : ",lunch)
print("TOTAL GUESTS COUNT IS : ",count)

#cost of breakfast
breakfast = lunch / 2
print("THE COST OF BREAKFAST IS : ",breakfast)

#cost of hall
hall =  (1/3) * lunch
hall = round(hall,2)
print("THE COST OF HALL IS : ",hall)

#cost of decoration
decor = (1/2) * hall
decor = round(decor,2)
print("THE COST OF DECORATION IS : ",decor)

#cost of parking
park = (1/10) * hall
park = round(park,2)
print("THE COST OF PARKING IS : ",park)

#total expense
tot_per_head = lunch + breakfast + hall + decor + park
tot_expense = tot_per_head * count
print("----------------------------------")
print("\n THE TOTAL EXPENSE PER HEAD IS : ",tot_per_head,"Rupees")
print("----------------------------------")
print("THE TOTAL EXPENSE FOR ",count," PEOPLE IS : ",tot_expense,"Rupees")

#amount sharing
huband_share = tot_expense / 2
#to check loan is nessecary
if(huband_share <= 50000):
    print("THERE IS NO NEED FOR LOAN")
else:
    loan = huband_share - 50000
    print("THERE IS NEED OF LOAN FOR RUPEES : ",loan)