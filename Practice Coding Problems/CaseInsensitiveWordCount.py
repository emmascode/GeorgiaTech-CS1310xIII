#Write a function called word_count. word_count should take
#as input a list. You may assume every item in the list will
#be a string.
#
#word_count should return a dictionary, where the keys are the
#words and the values are the number of times each word appeared
#in the list. The keys should all be lower-case, and you should
#ignore case when counting words (for instance, "cat", "CAT",
#and "Cat" would all count towards the key "cat").
#
#For example:
#
#  word_count(["cat", "CAT", "dog", "DOG"]) -> {"cat": 2, "dog": 2}
#  word_count(["Georgian", "Tech", "Georgia", "Tech"]) ->
#             {"Georgian": 1, "Tech": 2, "Georgia": 1}


#Write your function here!
def word_count(my_list):
    my_dict = {}
    for word in my_list:
        if word.lower() not in my_dict:
            if word not in my_dict:
                my_dict[word.lower()] = 1
            else:
                my_dict[word.lower()] += 1
        else:
            my_dict[word.lower()] += 1
    return my_dict


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{"cat": 2, "dog": 2}
#{"Georgian": 1, "Tech": 2, "Georgia": 1}
print(word_count(["cat", "CAT", "dog", "DOG"]))
print(word_count(["Georgian", "Tech", "Georgia", "Tech"]))


