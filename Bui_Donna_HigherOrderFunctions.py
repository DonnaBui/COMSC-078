# Higher Order Functions - Donna Bui - 2/22/2023 - Professor Henry Estrada's COMSC 078
# This program will prompt the user to enter lower and upper bounds and calculate the sum of all the squares, fourth powers, and square roots of the numbers between the lower and upper bounds.

def summation(f, lower, upper):
    """ This function accepts arguments that include a function, lower bound, and upper bound. It then sums the values from the function for each of the numbers between the lower bound and upper bound, inclusive """
    # revise and update the code from the summation function that was introduced in section 1.6 of the text.
    x = lower
    total = 0
    while x <= upper:
        total += f(x)
        x += 1
    return total
    
def square(x):
    """ This function calculates and returns the square of the input argument x """
    return x**2
         
def fourth_power(x):
    """ This function calculates and returns the fourth power of x. It uses neither x*x*x*x nor math.pow(x, 4) """
    return x**4

lambda_sqrt = lambda x: x**0.5
""" This function calculates and returns the square of x. It uses a lambda expression."""
   
    
def main():        
    low = int(input("Enter a lower bound for the sum: "))
    up = int(input("Enter an upper bound for the sum: "))

    squaretotal = summation(square, low, up)
    print("The sum of squares of the numbers from", low, "to", up, "is", squaretotal)
    fourthtotal = summation(fourth_power, low, up)
    print("The sum of squares of the numbers from", low, "to", up, "is", fourthtotal)
    sqrttotal = summation(lambda_sqrt, low, up)
    print("The sum of squares of the numbers from", low, "to", up, "is", sqrttotal)
    main()
    
main()
