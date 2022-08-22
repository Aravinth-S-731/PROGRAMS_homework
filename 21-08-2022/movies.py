#intial values
my_movies = []
friend_movies = []
common_movies = []
my_movies_count = int(input("ENTER THE NUMBER OF MOVIES WATCHED BY YOURSELF    : "))
friend_movies_count = int(input("ENTER THE NUMBER OF MOVIES WATCHED BY YOUR FRINED : "))

#to get my movies collection
for i in range(0,my_movies_count):
    temp_var = input("ENTER #" +str(i+1)+ " MOVIE YOU WATCHED : ")
    my_movies.append(temp_var)
#to get the input for friend
for i in range(0,friend_movies_count):
    temp_var = input("ENTER " +str(i+1)+ "st MOVIE YOU WATCHED BY YOUR FRIEND : ")
    friend_movies.append(temp_var)

print("MOVIES WATCHED BY MYSELF    : ",my_movies)
print("MOVIES WATCHED BY MY FRIEND : ",friend_movies,"\n")
#to find common movies watched by both
for i in range(0,my_movies_count):
    for j in range(0,friend_movies_count):
        if (my_movies[i] == friend_movies[j]):
            temp_var = my_movies[i]
            common_movies.append(temp_var)
#to print common movies
no_of_common_movies = len(common_movies)
if(no_of_common_movies == 0):
    print("NO COMMON MOVIES")
else:
    print("COMMON MOVIES : ")
    for i in range(0,no_of_common_movies):
        if(no_of_common_movies > 0):
            print(common_movies[i])

#---------- OUTPUT : 1 ----------
# ENTER THE NUMBER OF MOVIES WATCHED BY YOURSELF    : 5
# ENTER THE NUMBER OF MOVIES WATCHED BY YOUR FRINED : 3
# ENTER #1 MOVIE YOU WATCHED : ironman
# ENTER #2 MOVIE YOU WATCHED : captain america
# ENTER #3 MOVIE YOU WATCHED : spiderman
# ENTER #4 MOVIE YOU WATCHED : loki
# ENTER #5 MOVIE YOU WATCHED : hulk
# ENTER 1st MOVIE YOU WATCHED BY YOUR FRIEND : batman
# ENTER 2st MOVIE YOU WATCHED BY YOUR FRIEND : superman
# ENTER 3st MOVIE YOU WATCHED BY YOUR FRIEND : ironman
# MOVIES WATCHED BY MYSELF    :  ['ironman', 'captain america', 'spiderman', 'loki', 'hulk']
# MOVIES WATCHED BY MY FRIEND :  ['batman', 'superman', 'ironman']

# COMMON MOVIES :
# ironman
#---------- OUTPUT:2 ----------
# ENTER THE NUMBER OF MOVIES WATCHED BY YOURSELF    : 2
# ENTER THE NUMBER OF MOVIES WATCHED BY YOUR FRINED : 2
# ENTER #1 MOVIE YOU WATCHED : ironman
# ENTER #2 MOVIE YOU WATCHED : batman
# ENTER 1st MOVIE YOU WATCHED BY YOUR FRIEND : insurgent
# ENTER 2st MOVIE YOU WATCHED BY YOUR FRIEND : interstellar
# MOVIES WATCHED BY MYSELF    :  ['ironman', 'batman']
# MOVIES WATCHED BY MY FRIEND :  ['insurgent', 'interstellar']

# NO COMMON MOVIES