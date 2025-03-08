# Sequences Part 1: Driver’s License Exam - Donna Bui - 3/15/2023 - Professor Henry Estrada's COMSC 078
# This program will prompt the user to input a letter answer for 20 questions and then calculate how many questions were correct/incorrect, whether or not the user passed, and which questions they got wrong.

def get_answers():
    # Variables - List of student's answers and the question number
    answers = []
    questionNumber = 1
    
    # Loop to prompt student for letter answer up to question 20
    while questionNumber <= 20:
        ans = input("Enter answer to Question " + str(questionNumber) + ": ").upper()
        
        # Loop to ensure that the answer is a valid option. If not, prompt user to input a valid option.
        while not ans == "A" and not ans == "B" and not ans == "C" and not ans == "D" and not ans == "SKIP": 
            ans = input("Please enter either A, B, C, or D as your answer, or 'SKIP' to move on to the next question: ").upper()
        
        answers.append(ans)
        questionNumber += 1
    return answers

def check_answers(ans, correctAns, passingScore):
    # Let the user know their exam is being checked
    print("-------------------------------------------------")
    print("Your exam has been completed and submitted.") 
    print("Calculating results...") 
    
    # Variables
    questionChecked = 0 # Number of the question being checked
    questionsRight = 0 # Number of correct questions
    questionsWrong = [] # List to store all the numbers of the incorrectly answered questions
    
    # Loop to check the answer of each question
    while questionChecked < 20:
        if ans[questionChecked] == correctAns[questionChecked]:
            questionsRight += 1
        else:
            questionsWrong.append(questionChecked)
        questionChecked += 1
    
    # Print the results of the exam
    print("Number of correct answers: ", questionsRight)
    print("Number of incorrect answers: ", len(questionsWrong))
    if questionsRight < 20: # Only print list of incorrect questions if score is less than 20/20
        print("Questions answered incorrectly:", questionsWrong)
        
    # Determine whether or not student passed
    if questionsRight >= passingScore:
        print("You passed the test with a score of", questionsRight, "out of 20.")
    else:
        print("You did not pass the test. Your score is", questionsRight, "out of 20.")
    print("-------------------------------------------------")

def main():
    
    # Variables - Answer key and minimum passing score
    correctAnswers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B",
                      "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
    passingScore = 15
    
    # User Instructions
    print("---------------------------------------------------------")
    print("This is the written portion of the driver's license exam.")
    print("The examination consists of 20 multiple-choice questions.")
    print("You must answer", passingScore, "out of 20 questions correctly to pass.")
    print("For each question, input either A, B, C, or D as your answer, or SKIP to move on to the next question.")
    print("Questions that are skipped will automatically be marked wrong. Once you skip, you cannot go back.")
    print("---------------------------------------------------------")
    
    # Method calls
    ans = get_answers()
    check_answers(ans, correctAnswers, passingScore)
    
    # Ask user if they want to redo the exam
    redo = input("Would you like to redo the exam? (Y/N): ").upper()
    while not redo == "Y" and not redo == "N": # Loop until the user enters either Y or N
        redo = input("Would you like to redo the exam? (Please enter either Y or N): ").upper()
    if redo == "Y":
        main()
    elif redo == "N":
        print("Thank you for using this program! To do the exam again, simply restart the program.")
        
main() 