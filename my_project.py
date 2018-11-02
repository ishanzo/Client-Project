# Your project code here
# TODO make project
# array for index positions that will later be changed to the guests' names
table_seats = ['host', '1','2','3','4','5','6','7','8','9','10','hostess']
# function to check if the input is right
def ask_name_check(x):
    # if ask_name is a number
        if x.isnumeric() == True:
    # then print input is not a name please start again
            print(x+" is not a name! Please start all over again! Sorry!")
    # exits from the program
            exit()
# function to check if the input is right
def ask_rank_check(y):
    # if ask_rank is not a numeric value
    if y.isnumeric() == False:
    # then print start again
        print(y+" is not a rank. Please start again and enter a number from 1-10")
    # exits from the program
        exit()
# function to check if the input is right
def ask_gender_check(z):
# if ask_gender is not f or m
    if y != "f" or m:
    # print start again
        print("Please type 'f' or 'm' ")
        print("Start again!")
    # exits from the program
        exit()

# variables for the first guest
ask_name_1 = input("What is your guest's name? ")
ask_name_check(ask_name_1)
ask_gender_1 = input("What is your guest's gender?(f or m) ")
ask_gender_check(ask_gender_1)
ask_rank_1 = input("What is your guest's ranking? (1-10) ")
ask_rank_check(ask_rank_1)
# variables for the second guest
ask_name_2 = input("What is your guest's name? ")
ask_name_check(ask_name_2)
ask_gender_2 = input("What is your guest's gender?(f or m) ")
ask_gender_check(ask_gender_2)
ask_rank_2 = input("What is your guest's ranking? (1-10) ")
ask_rank_check(ask_rank_2)
# variables for the third guest
ask_name_3 = input("What is your guest's name? ")
ask_name_check(ask_name_3)
ask_gender_3 = input("What is your guest's gender?(f or m) ")
ask_gender_check(ask_gender_3)
ask_rank_3 = input("What is your guest's ranking? (1-10) ")
ask_rank_check(ask_rank_3)
# variables for the fourth guest
ask_name_4 = input("What is your guest's name? ")
ask_name_check(ask_name_4)
ask_gender_4 = input("What is your guest's gender?(f or m) ")
ask_gender_check(ask_gender_4)
ask_rank_4 = input("What is your guest's ranking? (1-10) ")
ask_rank_check(ask_rank_4)
# variables for the fifth guest
ask_name_5 = input("What is your guest's name? ")
ask_name_check(ask_name_5)
ask_gender_5 = input("What is your guest's gender?(f or m) ")
ask_gender_check(ask_gender_5)
ask_rank_5 = input("What is your guest's ranking? (1-10) ")
ask_rank_check(ask_rank_5)
# variables for the sixth guest
ask_name_6 = input("What is your guest's name? ")
ask_name_check(ask_name_6)
ask_gender_6 = input("What is your guest's gender?(f or m) ")
ask_gender_check(ask_gender_6)
ask_rank_6 = input("What is your guest's ranking? (1-10) ")
ask_rank_check(ask_rank_6)
# variables for the seventh guest
ask_name_7 = input("What is your guest's name? ")
ask_name_check(ask_name_7)
ask_gender_7 = input("What is your guest's gender?(f or m) ")
ask_gender_check(ask_gender_7)
ask_rank_7 = input("What is your guest's ranking? (1-10) ")
ask_rank_check(ask_rank_7)
# varibles for the eighth guest
ask_name_8 = input("What is your guest's name? ")
ask_name_check(ask_name_8)
ask_gender_8 = input("What is your guest's gender?(f or m) ")
ask_gender_check(ask_gender_8)
ask_rank_8 = input("What is your guest's ranking? (1-10) ")
ask_rank_check(ask_rank_8)
# variables for the ninth guest
ask_name_9 = input("What is your guest's name? ")
ask_name_check(ask_name_9)
ask_gender_9 = input("What is your guest's gender?(f or m) ")
ask_gender_check(ask_gender_9)
ask_rank_check(ask_rank_9)
ask_rank_9 = input("What is your guest's ranking? (1-10) ")
# variables for the tenth guest
ask_name_10 = input("What is your guest's name? ")
ask_name_check(ask_name_10)
ask_gender_10 = input("What is your guest's gender?(f or m) ")
ask_gender_check(ask_gender_10)
ask_rank_10 = input("What is your guest's ranking? (1-10) ")
ask_rank_check(ask_rank_10)
def table_seater(ask_name,ask_gender,ask_rank): # converts rank into seating positions (index position of table_seats array)
# table_seats = ['host', '1','2','3','4','5','6','7','8','9','10','hostess'] is the array whose index positions will be referred a lot to in this function
# Host and hostess sit at the head sets, at either end of the table.
    if ask_rank == 0:
        print("you are the host/ess")
# Ranking 1 sits to the right of the host
    elif ask_rank == '1':
# if the rank is 1, the index pos will be 1
        table_seats[1] = ask_name
# Ranking 2 sits at the right of the host
    elif ask_rank == '2':
# if the rank is 2, the index pos will be 10
        table_seats[10] = ask_name
# Ranking 3 sits left of the host
    elif ask_rank == '3':
# if the rank is 3, the index pos will be 6
        table_seats[6] = ask_name
# Ranking 4 sits left of the hostess
    elif ask_rank == '4':
# if the rank is 4, the index pos will be 5
        table_seats[5] = ask_name
# Ranking 5 sits at next to 1
    elif ask_rank == '5':
# if the rank is 5, the index pos will be 2
        table_seats[2] = ask_name
# Ranking 6 sits next next to Ranking 2
    elif ask_rank == '6':
# if the rank is 6, the index pos will be 9
        table_seats[9] = ask_name
# Ranking 7 sits next to Ranking 3
    elif ask_rank == '7':
        table_seats[7] = ask_name
# Ranking 8 sits next to Ranking 4
    elif ask_rank == '8':
        table_seats[4] = ask_name
# Ranking 9 sits next to Ranking 8
    elif ask_rank == '9':
        table_seats[3] = ask_name
# Ranking 10 sits between Ranking 7 and 6
    elif ask_rank == '10':
        table_seats[8] = ask_name
        print(table_seats)
    else:
# Can move onto the next line
        pass
# Calling the table_seater function (defined above) 10 times
table_seater(ask_name_1,ask_gender_1,ask_rank_1)
table_seater(ask_name_2,ask_gender_2,ask_rank_2)
table_seater(ask_name_3,ask_gender_3,ask_rank_3)
table_seater(ask_name_4,ask_gender_4, ask_rank_4)
table_seater(ask_name_5,ask_gender_5, ask_rank_5)
table_seater(ask_name_6,ask_gender_6, ask_rank_6)
table_seater(ask_name_7,ask_gender_7, ask_rank_7)
table_seater(ask_name_8,ask_gender_8, ask_rank_8)
table_seater(ask_name_9,ask_gender_9, ask_rank_9)
table_seater(ask_name_10,ask_gender_10, ask_rank_10)

print("This is what your table should look like")
# prints the new array of table seats with names instead of numbers
print(table_seats)
# prints a rectangle that looks like a table with assigned seats
print(table_seats[6],'_________',table_seats[7],'_________',table_seats[8],'________',table_seats[9],'_______',table_seats[10],'________')
print('''
         |                                                                      |
         |                                                                       |
         |                                                                      |
         |                                                                       | ''')

print("host",                                                                "hostess")
print('     |                                                                           | ')
print('     |                                                                           | ')
print('     |                                                                           | ')
print('     |                                                                           | ')
print('     |                                                                           | ')
print('     |                                                                           | ')
print(table_seats[1],'_________',table_seats[2],'__________',table_seats[3],'_________',table_seats[4],'________',table_seats[5],'___________________')
