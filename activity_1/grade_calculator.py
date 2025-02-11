# activity 1 - grade calculator

while True:
    while True:
        try: 
            grade = float(input("What is your grade? "))                # asks user input for a grade
            break
        except ValueError:                                              # in case the input is not a numerical value
            print("Please enter a valid numerical grade")

    if 90 <= grade <= 100:                                              # tests each case with an integer range
        print("A*")
    elif 80 <= grade <= 89:
        print("A")
    elif 70 <= grade <= 79:
        print("B")
    elif 60 <= grade <= 69:
        print("C")
    elif 50 <= grade <= 59:
        print("D")
    elif 0 <= grade <= 49:
        print("Fail")
    elif grade < 0:
        print("You can't score a negative grade genius")                # catches any invalid inputs that are less than 100%.
    else:
        print("You can't score more than 100% genius.")                 # catches any invalid inputs that are greater than 100%.

    again = input("Would you like to test another grade? Y/N").lower()
    if again != "y":
        print("Goodbye! Best wishes for your future exams!")
        break
    