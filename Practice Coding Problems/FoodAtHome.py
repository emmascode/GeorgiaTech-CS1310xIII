#You are going through your refrigerator at home and trying to determine whether you have the proper ingredients to cook a meal.
#
#Write a function called food_at_home. food_at_home should have one parameter, a list of foods in your house as strings. In order to cook a meal, the list must contain "cooking oil" and at least one other item. If this criteria is not met, return the string "I guess it's pizza tonight". If you do have cooking oil and at least one other food, return the string, "You do have food, your options are ... or ... or ...", where the ...s are replaced by the food names in the list in the order in which they appear. "cooking oil" should not be one of the foods listed under options.
#
#For example:
#food_list = ["chicken", "mixed veggies", "greens", "beans", "corn", "cooking oil"]
#food_at_home(food_list) -> "You do have food, your options are chicken or mixed veggies or greens or beans or corn"


#Write your code here!
def food_at_home(my_list):
    if not ('cooking oil' in my_list and len(my_list) >= 2):
        return "I guess it's pizza tonight"
    else:
        my_string = "You do have food, your options are " 
        for item in my_list:
            if item != "cooking oil":
                my_string += item + " or "
        return my_string[:-4]
        


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: You do have food, your options are chicken or mixed veggies or greens or beans or corn
food_list = ["chicken", "mixed veggies", "greens", "beans", "corn", "cooking oil"]
print(food_at_home(food_list))


