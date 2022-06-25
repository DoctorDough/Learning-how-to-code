# 1. Divisors: Create a program that asks the user for a number and then prints out a list of all the divisors of that number
#from https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

num_u = int(input('Number you want the dividers of '))

number_list = range (1, num_u +1)

Div_list = []

for number in number_list:
    if num_u % number is 0: 
        Div_list.append(number)

print (Div_list)

# 2. Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that 
#prints out all the elements of the list that are less than 5.
#from https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for number in a:
    if number < 5:
        print(number)

# 2.1 Instead of printing the elements one by one, make a new list that has all the elements less than 5 
#from this list in it and print out this new list.

b = []
for number in a: 
    if number < 5:
        b.append (number)
print (b)

# 2.2 Ask the user for a number and return a list that contains only elements from the original list a 
#that are smaller than that number given by the user.

c = []
num_u = int(input('Tell me a number '))
for number in a:
    if number < num_u:
        c.append(number)
print (c)
