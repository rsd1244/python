#Setting the variables that will be used to determine how many times the following words have been printed
foo = int(0)
bar = int(0)
fizz = int(0)
buzz = int(0)
fizzbuzz = int(0)
bazz = int(0)

#Forces the user to enter a number that is an integer and not zero
while 1:
    try:
        lower = int(input("Please Enter lower number... must not be zero\n"))
        if isinstance(lower, int) and lower > 0:
            break
    except:
        print("Please try again...\n")

#Forces the user to enter an integer that is greater than zero and greater than 'lower'.
while 1:
    try:
        upper = int(input("\nPlease Enter upper number...\n1:must not be zero \n2:Must be greater than lower\n"))
        if isinstance(upper, int) and upper > lower:
            break
    except:
        print("Please try again...\n")

#Loop to iterate starting at the lower number through the upper number (+ 1 because we want to check that number also)
for x in range(lower, upper + 1):
    temp = 0

    #Sequence of If statements to check if X has a remained when divided by the numbers. Print the word and increment the counter
    # Note: Temp is used to determine if any of the the operations had a match, if not, then that number didnt meet any of the requirements.
    if x % 30 == 0:
        print("foo")
        foo += 1
        temp = 1
    if x % 5 == 0:
        print("bar")
        bar += 1
        temp = 1
    if x % 3 == 0:
        print("fizz")
        fizz += 1
        temp = 1
    if x % 2 == 0:
        print("buzz")
        buzz += 1
        temp = 1
    if x % 3 == 0 and x % 2 == 0:
        print("fizzbuzz")
        fizzbuzz += 1
        temp = 1
    if temp == 0:
        print("bazz")
        bazz += 1

#Print out the information...

print("The total numbers evaluated was ", (upper + 1) - lower)
print("There were", foo, "numbers that are divisible by 30")
print("There were", bar, "numbers that are divisible by 5")
print("There were", fizz, "numbers that are divisible by 3")
print("There were", buzz, "numbers that are divisible by 2")
print("There were ", fizzbuzz, " numbers that are divisible by both 3 and 2.")
print("There were ", bazz, "numbers that didn't meet any of the requirements above.")
