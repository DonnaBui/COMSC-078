# Recursive Functions - Donna Bui - 3/2/2023 - Professor Henry Estrada's COMSC 078
# This program will prompt the user to enter lower and upper bounds and print all the numbers between the lower and upper bounds as well as calculate the sum of all the numbers between the two bounds.  

def display_em(lower, upper):
    """ This recursive function displays the consecutive integers from its lower to its upper bounds """
    if lower == upper:
        print(upper)
    else:
        print(lower)
        display_em(lower+1, upper)

def add_em(lower, upper):
    """ This recursive function calculates the sum of the consecutive integers from its lower to its upper bounds"""
    if lower == upper:
        return lower
    else:
        return lower + add_em(lower+1, upper)
    
def applyToEach(f, lower_bound, upper_bound):
    """ This higher-order function applies the included function to its lower and upper bound aruments"""
    return f(lower_bound, upper_bound)
         
def main():        
    low = int(input("Enter a lower bound: "))
    up = int(input("Enter an upper bound: "))
    print("All numbers between", low, "and", up, "are: ")
    applyToEach(display_em, low, up)
    totalsum = applyToEach(add_em, low, up)
    print("Sum of all numbers between", low, "and", up, "is", totalsum)

main()
 