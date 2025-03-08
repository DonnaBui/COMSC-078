# Test #1 Program - Donna Bui - 3/4/2023 - Professor Henry Estrada's COMSC 078
# This program will generate 100 random integers within the range of 1-1000 and print how many numbers are odd and how many are even.

import random

def isEven(num): 
    #This function will check whether or not a number is even using % and return true/false based on the result
    if num % 2 == 0:
        return True
    else:
        return False
    
def main(): # Main function
    
    # Variables
    nums = 0 
    odd = 0
    even = 0
    
    # Run the loop 100 times
    while not nums == 100: 
        currentNumber = random.randint(1, 1000)
        # print(currentNumber) #  ----  this is for debugging
        if isEven(currentNumber) == True:
            even += 1
            # print(currentNumber, "is even") #  ----  this is for debugging
        elif isEven(currentNumber) == False:
            odd += 1
            # print(currentNumber, "is odd") #  ----  this is for debugging
        nums += 1
    
    # Print results and prompt user if they want to run it again
    print("Out of 100 random numbers,", odd, "were odd, and", even, "were even.")
    userInput = input("Would you like to run the program again? (Y/N): ").lower()
    while not userInput == "y" and not userInput == "n": # Loop until the user enters either Y or N
        userInput = input("Would you like to run the program again? (Please enter Y or N): ").lower()
    if userInput == "y":
        main()
    elif userInput == "n":
        print("Thank you for using this program! To use it again, simply restart the program.")
        
main()