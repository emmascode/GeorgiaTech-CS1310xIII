#Write a function called get_grade that will read a
#given .cs1301 file and return the student's grade.
#To do this, we would recommend you first pass the
#filename to your previously-written reader() function,
#then use the list that it returns to do your
#calculations. You may assume the file is well-formed.
#
#A student's grade should be 100 times the sum of each
#individual assignment's grade divided by its total,
#multiplied by its weight. So, if the .cs1301 just had
#these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
#Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


#Write your function here!

def get_grade(input_file):
    open_input_file = open(input_file, "r")
    final_list = [] 
    for line in open_input_file:
        line = line.split()
        line[0] = int(line[0])
        line[2] = int(line[2])
        line[3] = int(line[3])
        line[4] = float(line[4])
        final_list.append(tuple(line))
    open_input_file.close()    
    final_grade = 0
    
    for line in final_list:
        total = line[2] * line[4] * 100/ line[3]
        final_grade += total
    
    return final_grade


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 91.55 
print(get_grade("sample.cs1301"))





