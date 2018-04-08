#Wayne Reilly 08/04/2018
#Write a Python script containing a function called factorial()
#Some help with earlier iterations of the script! https://codeyarns.com/2010/02/05/python-product-of-elements-of-a-list/
#More "inspriation" https://stackoverflow.com/questions/5136447/function-for-factorial-in-python

x = int(input("Please enter a number: ")) #I cannot get the function to accept this number!!!!

def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
 
print("The factorial of 5 is: ", factorial(5))
print("The factorial of 7 is: ", factorial(7))
print("The factorial of 10 is: ", factorial(10))

