# Functions Part 1: Statistical Functions - Donna Bui - 2/14/2023 - Professor Henry Estrada's COMSC 078

import math

def reciprocal(num): # reciprocal is one divided by the target number.
    return 1/num

def mean(num1, num2, num3):  # add all 3 numbers and divide by amount of numbers (3)
    return (num1+num2+num3)/3
   
def geometric_mean(num1, num2, num3): # multiply all 3 numbers and take cube root of product
    return math.pow(num1*num2*num3, (1/3))

def harmonic_mean(num1, num2, num3):
# Take reciprocal of all 3 numbers
    numA = reciprocal(num1)
    numB = reciprocal(num2)
    numC = reciprocal(num3)
# Divide 3 by the sum of the 3 reciprocals 
    return reciprocal(mean(numA,numB,numC))

def main():
    print("Reciprocal of 8 is", reciprocal(8), "[should be 0.125]")
    print("Reciprocal of 4/3 is", reciprocal(4/3), "[should be 0.75]")
    print("Reciprocal of -3 is", reciprocal(-3), "[should be -0.3333...]")
    print("Mean of 1, 13, 4 is", mean(1, 13, 4), "[should be 6.0]")
    print("Mean of -5, -12, -9 is", mean(-5, -12, -9), "[should be -8.666...]")
    print("Geometric mean of 144, 2, 6 is", geometric_mean(144, 2, 6), \
        "[should be 11.9999..]")
    print("Geometric mean of 2.1, 16.8, 16.8 is", geometric_mean(2.1, 16.8, 16.8), \
        "[should be 8.3.999...]")
    print("Harmonic mean of 1, 2, 3 is", harmonic_mean(1, 2, 3), \
        "[should be 1.636363...]")
    print("Harmonic mean of -2, 1, 1 is", harmonic_mean(-2, 1, 1), \
        "[should be 2.0]")
main()
