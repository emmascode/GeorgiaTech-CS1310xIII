#Write a function called average_evens_and_odds. The function
#should take as input one parameter, a list of integers. The
#function should return a 2-tuple. The first item in the
#2-tuple should be the average of all even numbers in the list;
#the second item in the 2-tuple should be the average of all
#odd numbers in the list. Round your averages to one decimal
#place.
#
#The list may have some strings interspersed in it. These should
#not affect your calculation.
#
#For example, if this was the input list:
#
# [1, 2, 3, 4, "cat", "tech", 5, 6]
#
#Your function would return the tuple: (4.0, 3.0) because 4.0
#is the average of the three even numbers (2, 4, 6) and 3.0 is
#the average of the three odd numbers (1, 3, 5).
#
#HINT: round(the_num, 1) will return the result of rounding
#the_num to one decimal place.


#Add your code here!
def average_evens_and_odds(my_list):
    sum_even  = []
    sum_odd = []
    for item in my_list:
        if str(item).isdigit() is True: 
            if item % 2 == 0:
                sum_even.append(item)
            else:
                sum_odd.append(item)
    a = round(sum(sum_even)/len(sum_even), 1)
    b = round(sum(sum_odd)/len(sum_odd), 1)
    return (a,b)


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (4.0, 3.0)
a_list = [1, 2, 3, 4, "cat", "tech", 5, 6]
print(average_evens_and_odds(a_list))





