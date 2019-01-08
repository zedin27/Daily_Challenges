#==========================================================================================#
#                                           PYTHON                                         # 
#                                     INTERACTIVE QUIZ 1                                   #
#                                         THE BASICS                                       # 
#                                    Written By: Kirk Worley                               #
#==========================================================================================#
#                                           OBJECTIVE                                      # 
#==========================================================================================#
#                                                                                          # 
#   In this interactive quiz of Python, you will be asked questions about the following    # 
#   lessons:                                                                               # 
#                                                                                          #        
#   General Foundations 1                                                                  # 
#   Functions                                                                              # 
#   Randomization                                                                          # 
#                                                                                          #
#==========================================================================================#
#                                           THE QUIZ                                       # 
#==========================================================================================#
#                                                                                          #
#   After you are done with the quiz, feel free to look over its structure and syntax.     # 
#   At the end of the quiz you will be given space to create a similar structured          # 
#   question and answer type activity of your own. You may copy/pase the quiz itself as    # 
#   a template for your own if you wish. For now, all you have to do is run the module.    #
#   You can press F5 or Run -> Run Module from this editing screen, or alternatively       #
#   you can double-click the "Python Basics Quiz 1.py" and run the actual program.         #
#   After the quiz you can return here.                                                    # 
#                                                                                          #
#==========================================================================================#
############################################################################################
#                                           BEGIN QUIZ CODE                                # 
############################################################################################

#---IMPORT RANDOM---#
import random

#---DEFINE INVALID RESPONSE---#
def inval():
    print "-----------------------------------"
    print "Please enter a valid response."
    print "-----------------------------------"
    pass

#---BEGIN MAIN CODE---#
print "Welcome to the 'Basics of Python' Quiz #1!"
print "These questions will test your general knowledge of Python from the lessons:"
print "General Foundations 1"
print "Funcions"
print "Randomization"
print "You will have 5 choices:"
print "A, B, C, D, or E which will always be 'None of the above'"
print "You will only get one chance to answer each question."
print "Good luck."

#---INPUT NAME---#
print "-----------------------------------"
name = raw_input("Name: ")
print "-----------------------------------"

#--SCORE VARIABLE--#
score = 0

#--QUIZ LOOP--#
quiz = 0

#---QUESTION 1---#
while (quiz == 0):
    print "Question 1:"
    print "What is a string?"
    print "A) Text, encased by quotes."
    print "B) Just Text."
    print "C) A number."
    print "D) A decimal number."
    print "E) None of the above."
    q1 = raw_input("Your answer: ")

    #--INTERPRET Q1--#
    if (q1.lower() == "a"):
        print "-----------------------------------"
        print "Correct."
        print "-----------------------------------"
        quiz = 1
        score += 1
    elif (q1.lower() == "b"):
        print "-----------------------------------"
        print "Incorrect."
        print "A string must have quotes around it. Otherwise it is a variable."
        print "-----------------------------------"
        quiz = 1
    elif (q1.lower() == "c"):
        print "-----------------------------------"
        print "Incorrect."
        print "A string must have quotes around it. Otherwise it is a variable."
        print "-----------------------------------"
        quiz = 1
    elif (q1.lower() == "d"):
        print "-----------------------------------"
        print "Incorrect."
        print "A string must have quotes around it. Otherwise it is a variable."
        print "-----------------------------------"
        quiz = 1
    elif (q1.lower() == "e"):
        print "-----------------------------------"
        print "Incorrect. "
        print "A string must have quotes around it. Otherwise it is a variable."
        print "-----------------------------------"
        quiz = 1
    else:
        inval()

#---QUESTION 2---#
while (quiz == 1):
    print "Question 2:"
    print "What is a variable?"
    print "A) A name."
    print "B) A number."
    print "C) Text, encased by quotes."
    print "D) An element we can reassign over and over."
    print "E) None of the above."
    q2 = raw_input("Your answer: ")

    #--INTERPRET Q2--#
    if (q2.lower() == "a"):
        print "-----------------------------------"
        print "Incorrect."
        print "A variable can be assigned to a value, string, or another variable."
        print "They can also be reassigned over and over."
        print "-----------------------------------"
        quiz = 2
    elif (q2.lower() == "b"):
        print "-----------------------------------"
        print "Incorrect."
        print "A variable can be assigned to a value, string, or another variable."
        print "They can also be reassigned over and over."
        print "-----------------------------------"
        quiz = 2
    elif (q2.lower() == "c"):
        print "-----------------------------------"
        print "Incorrect."
        print "A variable can be assigned to a value, string, or another variable."
        print "They can also be reassigned over and over."
        print "-----------------------------------"
        quiz = 2
    elif (q2.lower() == "d"):
        print "-----------------------------------"
        print "Correct."
        print "-----------------------------------"
        score += 1
        quiz = 2
    elif (q2.lower() == "e"):
        print "-----------------------------------"
        print "Incorrect."
        print "A variable can be assigned to a value, string, or another variable."
        print "They can also be reassigned over and over."
        print "-----------------------------------"
        quiz = 2
    else:
        inval()

#---QUESTION 3---#
while (quiz == 2):
    print "Question 3:"
    print "If at any point a colon ':' is used, you must ___ ?"
    print "A) Do nothing."
    print "B) Make sure the body of the code is indented."
    print "C) Put quotes around the body of the code."
    print "D) Leave an empty line in between each subsequent line."
    print "E) None of the above."
    q3 = raw_input("Your answer: ")

    #--INTERPRET Q3--#
    if (q3.lower() == "a"):
        print "-----------------------------------"
        print "Incorrect."
        print "A body of code must always be indented. A body of code is"
        print "always makred by a colon. ':'"
        print "-----------------------------------"
        quiz = 3
    elif (q3.lower() == "b"):
        print "-----------------------------------"
        print "Correct."
        print "-----------------------------------"
        score += 1
        quiz = 3
    elif (q3.lower() == "c"):
        print "-----------------------------------"
        print "Incorrect."
        print "A body of code must always be indented. A body of code is"
        print "always makred by a colon. ':'"
        print "-----------------------------------"
        quiz = 3
    elif (q3.lower() == "d"):
        print "-----------------------------------"
        print "Incorrect."
        print "A body of code must always be indented. A body of code is"
        print "always makred by a colon. ':'"
        print "-----------------------------------"
        quiz = 3
    elif (q3.lower() == "e"):
        print "-----------------------------------"
        print "Incorrect."
        print "A body of code must always be indented. A body of code is"
        print "always makred by a colon. ':'"
        print "-----------------------------------"
        quiz = 3
    else:
        inval()
    
#---QUESTION 4---#
while (quiz == 3):
    print "Question 4:"
    print "What phrase always comes BEFORE a function?"
    print "A) define"
    print "B) start"
    print "C) def"
    print "D) begin"
    print "E) None of the above."
    q4 = raw_input("Your answer: ")

    #--INTERPRET Q4--#
    if (q4.lower() == "a"):
        print "-----------------------------------"
        print "Incorrect."
        print "def is the correct preceding term."
        print "-----------------------------------"
        quiz = 4
    elif (q4.lower() == "b"):
        print "-----------------------------------"
        print "Incorrect."
        print "def is the correct preceding term."
        print "-----------------------------------"
        quiz = 4
    elif (q4.lower() == "c"):
        print "-----------------------------------"
        print "Correct."
        print "-----------------------------------"
        score += 1
        quiz = 4
    elif (q4.lower() == "d"):
        print "-----------------------------------"
        print "Incorrect."
        print "def is the correct preceding term."
        print "-----------------------------------"
        quiz = 4
    elif (q4.lower() == "e"):
        print "-----------------------------------"
        print "Incorrect."
        print "def is the correct preceding term."
        print "-----------------------------------"
        quiz = 4
    else:
        inval()

#---QUESTION 5---#
while (quiz == 4):
    print "Question 5:"
    print "What will this code print?"
    print " "
    print "a = 1"
    print "b = 2"
    print "a = 5"
    print "c = a + b"
    print "print c"
    print " "
    print "A) 3"
    print "B) 6"
    print "C) 7"
    print "D) This will result in an error."
    print "E) None of the above."
    q5 = raw_input("Your answer: ")

    #--INTERPRET Q5--#
    if (q5.lower() == "a"):
        print "-----------------------------------"
        print "Incorrect."
        print "a was re-assigned to 5."
        print "b = 2."
        print "5 + 2 = 7."
        print "-----------------------------------"
        quiz = 5
    elif (q5.lower() == "b"):
        print "-----------------------------------"
        print "Incorrect."
        print "a was re-assigned to 5."
        print "b = 2."
        print "5 + 2 = 7."
        print "-----------------------------------"
        quiz = 5
    elif (q5.lower() == "c"):
        print "-----------------------------------"
        print "Correct."
        print "-----------------------------------"
        score += 1
        quiz = 5
    elif (q5.lower() == "d"):
        print "-----------------------------------"
        print "Incorrect."
        print "a was re-assigned to 5."
        print "b = 2."
        print "5 + 2 = 7."
        print "-----------------------------------"
        quiz = 5
    elif (q5.lower() == "e"):
        print "-----------------------------------"
        print "Incorrect."
        print "a was re-assigned to 5."
        print "b = 2."
        print "5 + 2 = 7."
        print "-----------------------------------"
        quiz = 5
    else:
        inval()

#---QUESTION 6---#
while (quiz == 5):
    print "Question 6:"
    print "What will this code yield?"
    print " "
    print "import random"
    print "r = random.randint(1,5)"
    print "print r"
    print " "
    print "A) It will give an error, randint is not a command."
    print "B) A random number from 1 to 5. (1,2,3,4,5)"
    print "C) A random number from 2 to 4. (2,3,4)"
    print "D) It will not print anything, r was not properly assigned."
    print "E) None of the above."
    q6 = raw_input("Your answer: ")

    #--INTERPRET Q6--#
    if (q6.lower() == "a"):
        print "-----------------------------------"
        print "Incorrect."
        print "randint is a command of the random module."
        print "-----------------------------------"
        quiz = 6
    elif (q6.lower() == "b"):
        print "-----------------------------------"
        print "Correct."
        print "-----------------------------------"
        score += 1
        quiz = 6
    elif (q6.lower() == "c"):
        print "-----------------------------------"
        print "Incorrect."
        print "randint includes both endpoints."
        print "-----------------------------------"
        quiz = 6
    elif (q6.lower() == "d"):
        print "-----------------------------------"
        print "Incorrect."
        print "r was assigned to the randint command. Then we print r."
        print "Therefore, this is correct."
        print "-----------------------------------"
        quiz = 6
    elif (q6.lower() == "e"):
        print "-----------------------------------"
        print "Incorrect."
        print "The code will print a random number from 1 to 5."
        print "-----------------------------------"
        quiz = 6
    else:
        inval()

#---QUESTION 7---#
while (quiz == 6):
    print "Question 7:"
    print "What is a boolean?"
    print "A) A loop."
    print "B) An operator."
    print "C) A string."
    print "D) A true/false variable."
    print "E) None of the above."
    q7 = raw_input("Your answer: ")

    #--INTERPRET Q7--#
    if (q7.lower() == "a"):
        print "-----------------------------------"
        print "Incorrect."
        print "A boolean is a variable that is either true or false."
        print "-----------------------------------"
        quiz = 7
    elif (q7.lower() == "b"):
        print "-----------------------------------"
        print "Incorrect."
        print "A boolean is a variable that is either true or false."
        print "-----------------------------------"
        quiz = 7
    elif (q7.lower() == "c"):
        print "-----------------------------------"
        print "Incorrect."
        print "A boolean is a variable that is either true or false."
        print "-----------------------------------"
        quiz = 7
    elif (q7.lower() == "d"):
        print "-----------------------------------"
        print "Correct."
        print "-----------------------------------"
        score += 1
        quiz = 7
    elif (q7.lower() == "e"):
        print "-----------------------------------"
        print "Incorrect."
        print "A boolean is a variable that is either true or false."
        print "-----------------------------------"
        quiz = 7
    else:
        inval()

#---END---#
while (quiz == 7):
    print "This is the end of the quiz."
    print "Well, %s, thank you for taking this quiz." % name
    print "I hope it was helpful. Feel free to take it again"
    print "if you didn't get all the answers correct."
    print " "
    print "Your score: %d/7." % score
    print " "
    print "Thank you for taking the quiz!"
    #--MESSAGE FROM THE DEVELOPER--#
    print "Now, you can edit this code in IDLE and create your"
    print "own quiz, using this as a template. You can use this"
    print "code however you please. I encourage you to read"
    print "through this code and understand how it works."
    print "If you have any questions, again, feel free to"
    print "email me at kworley@csumb.edu."
    print "Thanks again."
    print " "
    print "-Kirk Worley"
    print "-----------------------------------"
    quiz = 8
    break;

############################################################################################
#                                           END OF QUIZ CODE                               # 
############################################################################################
