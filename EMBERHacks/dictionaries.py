from menu import *
commands = {
    'MENU': '''Below is the menu and the numbers corresponding to each menu item. 

1: hungry_marauder ($9.99)

2: pita_pocket ($6.50)

3: bridges_best ($11.50)

4: teriyaki_chicken ($12.50)

5: hammertown_soups ($9.95)

6: onion_rings ($2.99)

7: grilled_cheese ($3.99)

Input the number of the item you would like to purchase, please input only one number at a time." 

When you have finished your selection of items, type "PROCEED"
If you would like to cancel your order, type "CANCEL"
'''
}

menu_items = {
    '1': hungry_marauder,
    '2': pita_pocket,
    '3': bridges_best,
    '4': teriyaki_chicken,
    '5': hammertown_soups,
    '6': onion_rings,
    '7': grilled_cheese,
}

pita_pocket_options = {
    '1': 'falafel',
    '2': 'chicken'
}

bridges_best_options = {
    '1': 'Wedges',
    '2': 'Fries'
}

hammertown_soups_options = {
    '1': 'Tofu',
    '2': 'Grilled Chicken',
    '3': 'Braised Beef'
}

onion_rings = {
    '1': 'Without Sprite',
    '2': 'With Sprite'
}

