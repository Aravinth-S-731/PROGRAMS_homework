passengers_count,normal_passenger_count,senior_passenger_count = 0,0,0          #intial count
normal_passenger_cost,senior_passenger_cost = 0,0                               #intial cost
total_cost,one_way_cost , two_way_cost = 0 , 1000 , 1750                        #price of one and return ticket

def total_passengers():                                                         #to get the count of passengers
    global passengers_count , normal_passenger_count , senior_passenger_count   #declaring global variables
    passengers_count = int(input("ENTER THE TOTAL NUMBER OF PASSENGERS(both adult & senior) : "))
    senior_passanger_option = input("IS THERE A SENIOR PASSANGER WITH TRAVELING YOU (y/n) : ")
    if senior_passanger_option == "y":                                          #if senior passenger is present
        senior_passenger_count = int(input("ENTER THE COUNT OF SENIOR PASSANGERS WITH YOU : "))
    normal_passenger_count = passengers_count - senior_passenger_count          #normal passengers count

def ticket_booking():                                                           #to book tickets for the passengers
    global normal_passenger_cost,senior_passenger_cost,total_cost,ticket_type   #global variables
    ticket_type = int(input("SELECTION OPTION :\n1.ONE WAY TICKET  (1000/-)\n2.WITH RETURN TICKET (1000/- + 750/-)\n"))
    if ticket_type == 1:                                                        #for one way ticket
        ticket_type = "ONE WAY TICKET"
        normal_passenger_cost = normal_passenger_count * one_way_cost
        senior_passenger_cost = (senior_passenger_count * one_way_cost) * 0.5   #50% off for senior
    elif ticket_type == 2:                                                      #with return ticket
        ticket_type = "TWO WAY TICKET"
        normal_passenger_cost = normal_passenger_count * two_way_cost
        senior_passenger_cost = (senior_passenger_count * two_way_cost) * 0.5   #50% off for senior
    else:
        print("Please select a proper option")                                  #other than above two options
        ticket_booking()                                                        #call the function again/recursive function
    total_cost = normal_passenger_cost + senior_passenger_cost                  #total cost of all passengers

def above_4_offer():                                                            #function for people above count 4
    global total_cost                                                           #global variable
    total_cost = total_cost - (total_cost * 0.2)                                #total cost after discount

total_passengers()                                                              #call funtion to find passenger count
ticket_booking()                                                                #call function to book tickets
print("\t-----\nYOU CHOOSE "+ticket_type)                                       #one or two way tickets
print("THE COST OF ADULLT PASSANGERS IS : ",normal_passenger_cost)              #cost for normal passenger
if(senior_passenger_count > 0):                                                 #if senior passenger is traveling
    print("---SENIOR PASSANGER GETS A DISCOUT OF 50%---")
    print("THE COST OF SENIOR PASSANGERS IS : ",senior_passenger_cost)
if passengers_count >= 4:                                                       #if total passenger is 4 or more 20% off
    print("---SINCE THERE ARE 4 OR MORE PEOPLE YOU GET 20% OFFER ON TOTAL COST---")
    above_4_offer()                                                             #call funtion to find 20% off
    print("THE TOTAL COST AFTER 20% OFFER IS : ",total_cost)                    
else:
    print("THE TOTAL COST IS : ",total_cost)
"""
---------- OUTPUT:1 ----------
ENTER THE TOTAL NUMBER OF PASSENGERS(both adult & senior) : 6
IS THERE A SENIOR PASSANGER WITH TRAVELING YOU (y/n) : y
ENTER THE COUNT OF SENIOR PASSANGERS WITH YOU : 2
SELECTION OPTION :
1.ONE WAY TICKET  (1000/-)
2.WITH RETURN TICKET (1000/- + 750/-)
1
        -----
YOU CHOOSE ONE WAY TICKET
THE COST OF ADULLT PASSANGERS IS :  4000
---SENIOR PASSANGER GETS A DISCOUT OF 50%---
THE COST OF SENIOR PASSANGERS IS :  1000.0
---SINCE THERE ARE 4 OR MORE PEOPLE YOU GET 20% OFFER ON TOTAL COST---
THE TOTAL COST AFTER 20% OFFER IS :  4000.0
---------- OUTPUT:2 ----------
ENTER THE TOTAL NUMBER OF PASSENGERS(both adult & senior) : 6
IS THERE A SENIOR PASSANGER WITH TRAVELING YOU (y/n) : y
ENTER THE COUNT OF SENIOR PASSANGERS WITH YOU : 2
SELECTION OPTION :
1.ONE WAY TICKET  (1000/-)
2.WITH RETURN TICKET (1000/- + 750/-)
2
        -----
YOU CHOOSE TWO WAY TICKET
THE COST OF ADULLT PASSANGERS IS :  7000
---SENIOR PASSANGER GETS A DISCOUT OF 50%---
THE COST OF SENIOR PASSANGERS IS :  1750.0
---SINCE THERE ARE 4 OR MORE PEOPLE YOU GET 20% OFFER ON TOTAL COST---
THE TOTAL COST AFTER 20% OFFER IS :  7000.0
---------- OUTPUT:3 ----------
ENTER THE TOTAL NUMBER OF PASSENGERS(both adult & senior) : 4
IS THERE A SENIOR PASSANGER WITH TRAVELING YOU (y/n) : n
SELECTION OPTION :
1.ONE WAY TICKET  (1000/-)
2.WITH RETURN TICKET (1000/- + 750/-)
3
Please select a proper option
SELECTION OPTION :
1.ONE WAY TICKET  (1000/-)
2.WITH RETURN TICKET (1000/- + 750/-)
1
        -----
YOU CHOOSE ONE WAY TICKET
THE COST OF ADULLT PASSANGERS IS :  4000
---SINCE THERE ARE 4 OR MORE PEOPLE YOU GET 20% OFFER ON TOTAL COST---
THE TOTAL COST AFTER 20% OFFER IS :  3200.0
---------- OUTPUT:4 ----------
ENTER THE TOTAL NUMBER OF PASSENGERS(both adult & senior) : 15
IS THERE A SENIOR PASSANGER WITH TRAVELING YOU (y/n) : y
ENTER THE COUNT OF SENIOR PASSANGERS WITH YOU : 6
SELECTION OPTION :
1.ONE WAY TICKET  (1000/-)
2.WITH RETURN TICKET (1000/- + 750/-)
2
        -----
YOU CHOOSE TWO WAY TICKET
THE COST OF ADULLT PASSANGERS IS :  15750
---SENIOR PASSANGER GETS A DISCOUT OF 50%---
THE COST OF SENIOR PASSANGERS IS :  5250.0
---SINCE THERE ARE 4 OR MORE PEOPLE YOU GET 20% OFFER ON TOTAL COST---
THE TOTAL COST AFTER 20% OFFER IS :  16800.0
"""