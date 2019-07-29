sandwich_orders = ['patty melt', 'reuben', 'ham', 'turkey', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []


print('\nThe deli has run out of pastrami. Thank you for understanding.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print('Currently making your ' + current_sandwich.title() + ' sandwich.')
    finished_sandwiches.append(current_sandwich)

for finished_sandwich in finished_sandwiches:
    print("\nWe hope you enjoy your " + finished_sandwich.title() + ' sandwich!')
