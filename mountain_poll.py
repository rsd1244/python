responses = {}

#Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #Prompt the user for a Name and a response.
    name = input('\nWhat is your name? ')
    response = input('\nWhat mountain do you want to climb? ')

    #Store the inputs in a dictionary
    responses[name] = response

    #Find out if anyone else will be taking the poll.
    repeat = input('Would you like anyone else to take the poll? (yes|no) ')
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results of the poll.
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name, 'would like to climb', response + '.')
