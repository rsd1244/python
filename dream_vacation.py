responses = {}
polling_active = True

while polling_active:
    name = input('\nWhat is your name: ')
    vacation = input('\nWhere is your dream vacation location: ')

    responses[name] = vacation

    repeat = input('\nWould you like to add any other destinations? yes|no ')
    if repeat == 'no':
        polling_active = False

print('\n--- Poll Results ---')
for name, vacation in responses.items():
    print(name,'would like to go to', vacation,'for vacation.')
