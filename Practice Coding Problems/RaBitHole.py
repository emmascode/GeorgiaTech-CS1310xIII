#Write a function called rabbit_hole. rabbit_hole should have
#two parameters: a dictionary and a string. The string may be
#a key to the dictionary. The value associated with that key,
#in turn, may be another key to the dictionary.
#
#Keep looking up the keys until you reach a key that has no
#associated value. Then, return that key.
#
#For example, imagine if you had the following dictionary.
#This one is sorted to make this example easier to follow:
#
# d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
#      "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
#      "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
#      "rat": "ram", "ram": "rat"}
#
#If we called rabbit_hole(d, "bat"), then our code should...
#
# - Look up "bat", and find "pig"
# - Look up "pig", and find "cat"
# - Look up "cat", and find "dog"
# - Look up "dog", and find "ant"
# - Look up "ant", and find no associated value, and so it would
#   return "ant".
#
#Other possible results are:
#
# rabbit_hole(d, "bat") -> "fly"
# rabbit_hole(d, "ewe") -> "hen"
# rabbit_hole(d, "jay") -> "doe"
# rabbit_hole(d, "yak") -> "yak"
#
#Notice that if the initial string passed in is not a key in
#the dictionary, that string should be returned as the result as
#well.
#
#Note, however, that it is possible to get into a loop. In the
#dictionary above, rabbit_hole(d, "rat") would infinitely go
#around between "rat" and "ram". You should prevent this: if a
#key is ever accessed more than once (meaning a loop has been
#reached), return the boolean False.
#
#Hint: If you try to access a value from a dictionary that does
#not exist, a KeyError will be raised.


#Write your function here!
def rabbit_hole(data_set, target_string):
    try:
        if type(target_string) == list:
            previous_key = target_string[0]
            target_string = target_string[-1]
            if previous_key == data_set[target_string]:
                return False

        key_value = []
        key_value.append( target_string )
        key_value.append( data_set[target_string] )
        return rabbit_hole(data_set, key_value)
    except KeyError:
        return target_string


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ant, hen, doe, yak, False, each on their own line.
d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
     "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
     "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
     "rat": "ram", "ram": "rat"}

print(rabbit_hole(d, "bat"))
print(rabbit_hole(d, "ewe"))
print(rabbit_hole(d, "jay"))
print(rabbit_hole(d, "yak"))
print(rabbit_hole(d, "rat"))


