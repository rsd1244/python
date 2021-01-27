#import required libraries
import time
import random

#main loop to keep the program running.
while 1:
    #generate random int between 1 and 9
    randomInt = random.randint(1, 9)
    question = input("Ask the magic 8 ball a question. ")

    #This loop forces the user to input something instead of leaving the question blank by checking length of question.
    #If question length is 0, reask the question.
    while len(question) == 0:
        question = input("Ask the magic 8 ball a question. ")

    #Wait for 5 seconds
    time.sleep(5)
    print("Searching for an answer...")
    print("Please please patient...")

    #Loop waiting... 10 times while waiting .5 seconds between each print
    for x in range(10):
        print("Waiting...")
        time.sleep(.5)

    #Wait 1 second
    time.sleep(1)

    #Decide what the magic 8 ball says based on the random integer generated at the beginning.
    if randomInt == 1:
        print("Maybe")
    elif randomInt == 2:
        print("Uncertain")
    elif randomInt == 3:
        print("Unlikely")
    elif randomInt == 4:
        print("Ask again later")
    elif randomInt == 5:
        print("Most Definitely.")
    elif randomInt == 6:
        print("Certainly")
    elif randomInt == 7:
        print("Yes")
    elif randomInt == 8:
        print("Cannot be determined")
    elif randomInt == 9:
        print("No")

    #Loop to force user to answer "ask another question" with a y or a n.
    while 1:
        choice = input("Ask another question? y for yes, n for no")
        #if yes, then y or Y will break out of this loop and redo the program from the beginning
        if choice == 'y' or choice == 'Y':
            break
        #If no, then n or N will print "Goodbye" and exit the program with code 0
        elif choice == 'n' or choice == 'N':
            print("Goodbye...")
            time.sleep(3)
            exit(0)
