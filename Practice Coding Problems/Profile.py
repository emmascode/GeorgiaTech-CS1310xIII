#Write a function called complete_profile. complete_profile
#will take as input a dictionary. This dictionary will have
#four keys: first, middle, last, and title. The function
#should return a dictionary with those four keys, and three
#more: name, full_name, short_name. The values for those
#keys should be:
#
# - name: the first and last name, separated by a space
# - full_name: the title, first, middle, and last names,
#   with a space between each pair of strings
# - short_name: the first letter of the first name, a space,
#   and their last name
#
#For example:
#
# complete_profile({"first": "David", "middle": "Andrew",
#                   "last": "Joyner", "title": "Dr."})
#
# would return:
#
# {"first": "David", "middle": "Andrew", "last": "Joyner",
#  "title": "Dr.", "name": "David Joyner",
#  "full_name": "Dr. David Andrew Joyner",
#  "short_name": "D Joyner"}
#
#You may either modify the dictionary that is passed in,
#or create a new one. Either way, make sure to return the
#dictionary at the end of the function.


#Add your code here!
def complete_profile(my_dict):
    new_dict = {}
    new_dict['first'] = my_dict['first']
    new_dict['middle'] = my_dict['middle']
    new_dict['last'] = my_dict['last']
    new_dict['title'] = my_dict['title']
    new_dict['name'] = my_dict['first'] + ' ' + my_dict['last']
    new_dict['full_name'] = my_dict['title'] + ' ' + my_dict['first'] + ' ' + my_dict['middle'] + ' ' + my_dict['last']
    new_dict['short_name'] = my_dict['first'][0] + ' ' + my_dict['last']
    return new_dict


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print "David Joyner", "Dr. David Andrew Joyner", and
#"D Joyner" each on a different line (without the quotes).
prof = {"first": "David", "middle": "Andrew", "last": "Joyner", "title": "Dr."}
prof = complete_profile(prof)
print(prof["name"])
print(prof["full_name"])
print(prof["short_name"])





