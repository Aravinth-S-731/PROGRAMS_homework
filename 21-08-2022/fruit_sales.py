#gettinf supply from user
supply_apples = int(input("ENTER THE SUPPLY OF APPLE : \t"))
supply_oranges = int(input("ENTER THE SUPPLY OF ORANGES : \t"))
supply_otherfruits = int(input("ENTER THE SUPPLY OF OTHER FRUIT :"))

#apple sales on monday , tuesday , wednesday. Price on 1nos. apple = 25
apple_sold = supply_apples * 0.5                #50% apple sales on monday
supply_apples -= apple_sold                     #modifying supply after sales
price_monday_apple = 25 * apple_sold
apple_sold = supply_apples                      #100% of apple sold on tuesday
supply_apples -= apple_sold                     #modifying supply after sales
price_tuesday_apple = 25 * apple_sold
price_wednesday_apple = 25 *supply_apples
total_apple = price_monday_apple + price_tuesday_apple + price_wednesday_apple

#orange sales on monday , tuesday , wednesday. Prince of 1nos. orange = 15
orange_sold = supply_oranges * 0.5              #50% of oranges sold on monday
supply_oranges -= orange_sold                   #modifying supply after sales
price_monday_orange = 15 * orange_sold
orange_sold = supply_oranges * 0.75             #75% of oranges sold on tuesday
supply_oranges -= orange_sold                   #modifying supply after sales
price_tuesday_orange = 15 * orange_sold
orange_sold = supply_oranges                    #all oranges are sold out
supply_oranges -= orange_sold                   #modifying supply after sales
price_wednesday_orange = 15 * orange_sold
total_orange = price_monday_orange + price_tuesday_orange + price_wednesday_orange

#otherfruit sales on monday , tuesday , wednesday. price is 10 per nos
otherfruit_sold = 10                            #10 nos sold
supply_otherfruits -= otherfruit_sold           #modifying supply after sales
price_monday_otherfruits = 10 * otherfruit_sold
otherfruit_sold = 30                            #30 nos sold
supply_otherfruits -= otherfruit_sold           #modifying supply after sales
price_tuesday_otherfruits = 10 * otherfruit_sold
otherfruit_sold = supply_otherfruits            #all fruits sold out
supply_otherfruits -= otherfruit_sold           #modifying supply after sales
price_wednesday_otherfruits = 10 * otherfruit_sold
total_otherfruits = price_monday_otherfruits + price_tuesday_otherfruits + price_wednesday_otherfruits

#sales into
print("DAY           \tMONDAY      \tTUESDAY      \tWEDNESDAY")
print("APPLE :       \t",price_monday_apple,"\t",price_tuesday_apple,"\t",price_wednesday_apple)
print("ORANGES :     \t",price_monday_orange," \t",price_tuesday_orange," \t",price_wednesday_orange)
print("OTHERFRUITS : \t",price_monday_otherfruits,"   \t",price_tuesday_otherfruits,"   \t",price_wednesday_otherfruits)
print("TOTAL :       \t",total_apple,"\t",total_orange,"\t",total_otherfruits)
print("TOTAL INCOME : ",total_apple + total_orange + total_otherfruits)

""" ---------- OUTPUT:1 ----------
ENTER THE SUPPLY OF APPLE :     100
ENTER THE SUPPLY OF ORANGES :   100
ENTER THE SUPPLY OF OTHER FRUIT :100
DAY             MONDAY          TUESDAY         WEDNESDAY
APPLE :          1250.0          1250.0          0.0
ORANGES :        750.0           562.5           187.5
OTHERFRUITS :    100             300             600
TOTAL :          2500.0          1500.0          1000
TOTAL INCOME :  5000.0
    ---------- OUTPUT ----------
ENTER THE SUPPLY OF APPLE :     50
ENTER THE SUPPLY OF ORANGES :   75
ENTER THE SUPPLY OF OTHER FRUIT :40
DAY             MONDAY          TUESDAY         WEDNESDAY
APPLE :          625.0           625.0           0.0
ORANGES :        562.5           421.875         140.625
OTHERFRUITS :    100             300             0
TOTAL :          1250.0          1125.0          400
TOTAL INCOME :  2775.0
 """