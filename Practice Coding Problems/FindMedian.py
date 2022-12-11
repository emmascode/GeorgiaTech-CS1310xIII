#Write a function called find_median. find_median
#should take as input a string representing a filename.
#The file corresponding to that filename will be a list
#of integers, one integer per line. find_median should
#return the median of the numbers in the file.
#
#If there is an odd number of values in the file, then
#find_median will return the middle value from the numbers
#in the file after they're sorted.
#
#If there is an even number of values in the file, then
#find_median should return the average of the two middle
#values after they're sorted.
#
#For example, in the dropdown in the top left you'll find a
#file named FindMedianInput.txt. There are 19 numbers in
#this file, so the median is the value at index 10 after
#sorting them: 16.
#
#You may assume that all lines in the file will contain a
#positive integer (greater than 0). There may be duplicates.


#Write your function here!
def find_median(file_name):
    file_input = open(file_name, 'r')
    my_list = []
    int_list = []
    for line in file_input:
        line_strip = line.strip('\n')
        my_list.append(line_strip)
    for char in my_list:
        int_list.append(int(char))
        int_list.sort()       
    #return int_list
    n = len(int_list)
    index = int(round(n/2, 0))
   
    if n % 2 == 1:
        return int_list[index-1]
    else:
        return (int_list[index] + int_list[index-1])/2
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 16
print(find_median("FindMedianInput.txt"))


