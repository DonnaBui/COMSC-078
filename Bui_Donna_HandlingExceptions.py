# Handling Exceptions - Donna Bui - 4/25/2023 - Professor Henry Estrada's COMSC 078
# This program will prompt the user for values of different types and handle exceptions / print an error message if the user provides an invalid type
# It will work for integers, floats, complex numbers, and Fractions.

from fractions import Fraction

def readInt(x):
    try:
        return int(x)
    except ValueError:
        print("Error: Value is not an integer.")
    
def readVal(valType, prompt, error):
        try:
            return valType(input(prompt))
        except ValueError:
            print(error)

def main():
    intVal = str(readInt(input('Enter an integer value: ')))
    print("intVal:", intVal, "\n")

    intVal2 = str(readVal(int, 'Enter an integer: ', 'Error: Value is not an integer.'))
    print("intVal2:", intVal2, "\n")

    floatVal = str(readVal(float, 'Enter a float value: ', 'Error: Value is not a float.'))
    print("floatVal:", floatVal, "\n")

    complexVal = str(readVal(complex, 'Enter a complex number: ', 'Error: Value is not a complex number.'))
    print("complexVal:", complexVal, "\n")

    fractionVal = str(readVal(Fraction, 'Enter a Fraction: ', 'Error: Value is not a Fraction.'))
    print("fractionVal:", fractionVal, "\n")
    
main()