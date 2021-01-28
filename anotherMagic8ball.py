#import required libraries
import time, random

# Varible to see if the program will be run again
again = True

#main loop to keep the program running.
while again:
    #generate random int between 1 and 9
    randomInt = random.randint(1, 9)
    print("Ask the magic 8 ball a question.")
    time.sleep(.5)

    question = input("Enter your question here >>>> ")

    #This loop forces the user to input something instead of leaving the question blank by checking length of question.
    #If question length is 0, reask the question.
    while len(question) == 0:
        question = input("Enter your question here >>>>  ")

    #Wait for 2 seconds
    time.sleep(2)
    print("Searching for an answer...")
    

    #Loop Searching... 10 times while waiting .5 seconds between each print
    for x in range(10):
        print("Searching...")
        time.sleep(.5)

    #Wait 1 second
    time.sleep(1)
    
    print("Answer to follow below:")
    time.sleep(3)
    
    #Decide what the magic 8 ball says based on the random integer generated at the beginning.
    if randomInt == 1:
        print("Answer: It is certainly possible!")
    elif randomInt == 2:
        print("Answer: It is decidedly so!")
    elif randomInt == 3:
        print("Answer: Reply Hazy, Try again")
    elif randomInt == 4:
        print("Answer: Ask again later")
    elif randomInt == 5:
        print("Answer: Most Definitely")
    elif randomInt == 6:
        print("Answer: I think NOT!")
    elif randomInt == 7:
        print("Answer: Yes")
    elif randomInt == 8:
        print("Answer: Cannot be determined")
    else:
        print("Answer: Outlook, not so good")

    time.sleep(2)

    #Loop to force user to answer "ask another question" with a y or a n.

    choice = input("Would you like to ask the Magic 8 ball another question? Press 'y' for yes or 'n' for no >>> ")
    while len(choice) == 0:
        choice = input("Would you like to ask the Magic 8 ball another question? Press 'y' for yes or 'n' for no >>> ")
        #if yes, then y or Y will break out of this loop and redo the program from the beginning
    if choice == 'y' or choice == 'Y':
        again = True
        #If no, then n or N will print "Goodbye" and exit the program with code 0
    elif choice == 'n' or choice == 'N':
        again = False
        print("Goodbye...")
        time.sleep(1)
