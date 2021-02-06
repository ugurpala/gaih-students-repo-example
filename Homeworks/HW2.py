"""
Homework 2

Ask the user to input a single digit integer to a variable a variable 'n'
Then, print out all of the even numbers from 0 to n (including n)

"""

n = int(input("Please enter a single digit integer: "))

while n<0 or n>9:

    print("Invalid number!!")
    n = int(input("Please enter a single digit integer: "))
    
even_numbers = list()

for i in range(0,n+1):
    if i % 2 == 0:
        even_numbers.append(i)
        print(i)
print("All of the even numbers from 0 to {} = {}".format(n, even_numbers))

