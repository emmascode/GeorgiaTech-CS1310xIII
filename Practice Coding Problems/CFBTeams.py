#Write a function called write_teams. write_teams will take
#as input two parameters: a string and a list of 4-tuples.
#
#The string will represent the filename to which to write.
#
#Each 4-tuple in the list will contain four strings. The
#strings will represent (in order) a university name, their
#team mascot, their city, and their state.
#
#write_teams should write the list of teams to the file given
#by the filename using the following format:
#
# [university] [mascot], [city], [state]
#
#Note there is no comma between university and mascot, but
#there is a comma between mascot and city, and city and state.
#
#So, for this list:
#
# [("Georgia Tech", "Yellow Jackets", "Atlanta", "Georgia"),
#  ("Georgia State", "Panthers", "Atlanta", "Georgia")]
#
#The file printed would look like this:
#
#Georgia Tech Yellow Jackets, Atlanta, Georgia
#Georgia State Panthers, Atlanta, Georgia
#
#We've included Sample.txt to show you what one of these
#files should look like.


#Write your function here!
def write_teams(file_name, my_list):
    file_input = open(file_name, 'w')
    for tup in my_list:
        file_input.write(tup[0] + ' ' + tup[1] + ', ' + tup[2] + ', ' + tup[3] + '\n')
    return file_input


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing -- however, it should write the same contents
#as Sample.txt to Test.txt.
teams = [("Georgia Tech", "Yellow Jackets", "Atlanta", "Georgia"), ("Georgia State", "Panthers", "Atlanta", "Georgia"),
        ("Kennesaw State", "Owls", "Kennesaw", "Georgia"), ("Georgia Southern", "Eagles", "Statesboro", "Georgia")]
write_teams("Test.txt", teams)



