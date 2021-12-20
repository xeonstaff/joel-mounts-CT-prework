#Joel Mounts prework for January 4th Cohort - Codingtemple 


#Question1
#given input 'username', prints username 

from typing import ValuesView


def hello_username(user_name):
    print("hello_" + user_name)

#Question 1 TEST
hello_username('AARON the aardvark')

#Question2
#returns the odd numbers from 0 to 100

def first_odds():
    x  = [*range(1,100,2)]
    print(x)

#Question 2 TEST
first_odds()

#Question3
#returns the maximum number in a list, given a_list

def max_num_in_list(a_list):
    return(max(a_list))

#Question3 TEST
y=[-100,0,1,2,3,88]
print(max_num_in_list(y))


#Question4
#given a year integer, returns TRUE if the year is a leap year
#--> definitely possible to do in one if/else statement, but I couldn't figure it out

def is_a_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else: 
        return False

#Question4 TEST
print(is_a_leap_year(2000)) #True
print(is_a_leap_year(1999)) #False
print(is_a_leap_year(2100)) #False
print(is_a_leap_year(12)) #False


#Question5
#given a list of integers, returns TRUE if the list is consecutive
#-->this solution seems clunky & incomplete, but it passes my simple tests so 
#-->future tests/errors: non-integers, other datatypes, etc. 

def is_consecutive(a_list):
    b_list = a_list[1:]
    for place, value in enumerate(a_list):
        if b_list[place] - a_list[place] == 1:
            return True
        else:
             return False

## Question5 TEST
b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #TRUE
print(is_consecutive(b_list))

c_list = [1, 4, 7, 1, 99, 1, 0] #FALSE
print(is_consecutive(c_list))

d_list = [-11, -50, 41, 2, 100, 10000, 1, -1, 0] #FALSE
print(is_consecutive(d_list))

