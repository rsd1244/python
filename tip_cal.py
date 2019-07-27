#!/usr/bin/env python3

total = float(input('Enter your total before tip: '))

tip_amount = float(input('Enter the percentage you would like to tip: '))

tip_conv = tip_amount * .01

tip = total * tip_conv

total_with_tip = total + tip

print('Your total with tip is ', str(total_with_tip) + '.')
