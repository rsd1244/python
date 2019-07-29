sandwich_orders = ['patty melt', 'reuben', 'ham', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print('Currently making your ' + current_sandwich.title() + ' sandwich.')
    finished_sandwiches.append(current_sandwich)

for finished_sandwich in finished_sandwiches:
    print("\nWe hope you enjoy your " + finished_sandwich.title() + ' sandwich!')
    
