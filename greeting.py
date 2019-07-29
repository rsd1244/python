def greeting():
    print('What is your name?')
    user = input()
    if user == 'Ritchie':
        print('Hello ' + user + ' welcome to python3')
    else:
        print('You\'re not Ritchie, you\'re ' + user + '! Go Away!!!')

greeting()
