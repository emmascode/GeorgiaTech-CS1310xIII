#We've given you a file called "top500.txt" which contains
#the name and lifetime gross revenue of the top 500
#films at the time this question was written. 
#
#Each line of the given file is formatted like so:
# <name>\t<gross revenue in dollars>
#
#In other words, you should call .split("\t") to split
#the line into the movie name (the first item) and the
#gross (the second item).
#
#Unfortunately, these movies are not in order. Write a 
#function called "sort_films" that accepts two parameters:
#a string of a source filename and a string of a
#destination filename. Your function should open the
#source file and sort the contents from greatest gross
#revenue to least gross revenue, and write the sorted
#contents to the destination filename. You may assume the
#source file is correctly formatted.
#
#Hint: one common issue on this problem is that every line
#in the input file ends with a line break except the last
#one. If the autograder gives you an index error, open
#top500result.txt and make sure there are 500 lines in your
#output file!


#Write your function here!
def sort_films(source_filename, destination_filename):
    source_filename = open(source_filename, "r")
    destination_filename = open(destination_filename, "w")
    movie_list = []
    for aVal in source_filename:
        aVal = aVal.strip("\n")
        aVal= aVal.split("\t")   
        movie_name = aVal[0]
        movie_gross = aVal[1]
        aTuple = (movie_name, movie_gross)
        movie_list.append(aTuple)
    movie_list.sort(reverse=True, key=lambda x:x[1])
    source_filename.close()
    for aTup in movie_list:
        each_line = str(aTup[0] + "\t" + aTup[1])
        destination_filename.write(each_line + '\n')
    destination_filename.close()
        
    

#The line of code below will test your function and put
#your results in top500result.txt. Then, it will print
#"Done!"
sort_films("top500.txt", "top500result.txt")
print("Done!")





