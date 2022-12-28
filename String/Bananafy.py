def bananafy(string):
    vowel_lower = "aeiou"
    vowel_upper = "AEIOU"
    new_string = ""
    for i in string:
        if i in vowel_lower:
            new_string += vowel_lower[vowel_lower.index(i) - 1]
        elif i in vowel_upper:
            new_string += vowel_upper[vowel_upper.index(i) - 1]
        else:
            new_string += i
    return new_string
print(bananafy("banana"))
print(bananafy("bununu"))
print(bananafy("I don't want that"))