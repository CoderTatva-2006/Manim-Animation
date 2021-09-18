# Python Program Showcasing list comprehensions
# Equivalent to set builder from in mathematical sets
# Task : print a list of squares from 0 to 10 

############ Normal Approach #############

list_of_squares = []

for num in range(11):
    list_of_squares.append(num**2)

print(list_of_squares) # [0,1,4,9,16,25,36,49,64,81,100]

############ List comprehension ##########

list_of_squares = [ num**2 for num in range(11) ] 

print(list_of_squares) # [0,1,4,9,16,25,36,49,64,81,100]

#######################################################