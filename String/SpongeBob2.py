#In the previous problem, you wrote a function that would
#convert text like "abcd efgh ijkl" into "AbCd eFgH IjKl".
#
#In the previous problem, you could assume the original
#string would be all lower-case, with no punctuation.
#
#Revise your function so that it no longer makes these
#assumptions. It should leave any punctuation marks or
#numerals unchanged, and it should change the case of
#every letter at an even index. That means if the letter
#is initially uppercase, it should be converted to lower
#case.
#
#For example: mock("Abcd. Efgh.. Ijkl!") would return
#"abCd. efGh.. IJkL!". The even-index letters (A, C, E, g,
#j, l) changed case, all other characters were unchanged.
#
#HINT: Lowercase letters always have an ordinal between
#97 ("a") and 122 ("z"). Uppercase letters always have an
#ordinal between 65 ("A") and 90 ("Z").


#Write your function here!
def mock(word):
    index = 0
    result = ''
    for letter in word:
        if index % 2 == 0:
            if letter.isupper():
                result += letter.lower()
            else:
                result += letter.upper()
        else:
            result += letter
        index += 1
    return result


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "abCd. efGh.. IJkL!".

print(mock("Abcd. Efgh.. Ijkl!"))



