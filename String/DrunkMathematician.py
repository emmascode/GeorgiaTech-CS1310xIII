#Write a function called to_metric. to_metric should take
#as input one parameter, a string. The string will represent
#a quantity in imperial volume units, such as "7 cups", "2
#tablespoons", or "8 gallons". to_metric should return the
#equivalent number of milliliters as a float. Round the
#result to two decimal places.
#
#The possible imperial units to handle and their conversion to
#milliliters are:
#
# - gallons: 3785.41 milliliters
# - quarts: 946.35 milliliters
# - pints: 473.18 milliliters
# - cups: 240 milliliters
# - ounces: 29.57 milliliters
# - tablespoons: 14.79 milliliters
# - teaspoons: 4.93 milliliters
#
#Return only the float representing the number of milliliters,
#not the label. For example:
#
#to_metric("7.0 cups") -> 1680
#to_metric("2.0 tablespoons") -> 29.58
#to_metric("8.0 gallons") -> 30283.28
#
#You may assume that the string will be formatted like the
#strings above: a decimal number, then a space, then one of
#the following words: cgallons, quarts, pints, cups, ounces,
#tablespoons, teaspoons


#Add your code here!
def to_metric(my_string):
    if my_string[-4:] == 'cups':
        return round(float(my_string[:4]) * 240, 2)
    elif my_string[-11:] == 'tablespoons':
        return round(float(my_string[:4]) * 14.79, 2)
    elif my_string[-6:] == 'quarts':
        return round(float(my_string[:4]) * 946.35, 2)
    elif my_string[-5:] == 'pints':
        return round(float(my_string[:4]) * 473.18, 2)
    elif my_string[-6:] == 'ounces':
        return round(float(my_string[:4]) * 29.57, 2)
    elif my_string[-9:] == 'teaspoons':
        return round(float(my_string[:4]) * 4.93, 2)
    else:
        return round(float(my_string[:4]) * 3785.41, 2)
    
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#1680
#29.58
#30283.28
print(to_metric("7.0 cups"))
print(to_metric("2.0 tablespoons"))
print(to_metric("8.0 gallons"))


