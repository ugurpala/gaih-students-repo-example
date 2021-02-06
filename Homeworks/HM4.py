  
"""
Homework 4

Finding prime numbers between 0 and 100 using functions

"""

def primenumber():
    
    primenumbers =list()
    
    for num in range(2,101):  
       
        for i in range(2,num):  
            if (num % i) == 0:  
                break  
        else:  
            primenumbers.append(num)
    print(primenumbers)
               

primenumber()
