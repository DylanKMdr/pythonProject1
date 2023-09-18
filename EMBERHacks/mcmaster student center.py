from menu import *
from dictionaries import *
purchase_complete = False
menu_opened = False
at_checkout = False
command = ''
command2 = ''
subtotal = 0
tax = 0
total = 0
items = []
checkout = f'''Your final purchase is:'''
print('''Welcome to Mcmaster Student Centre! 
If you would like to see the menu, type "MENU"
''')
while not at_checkout and not menu_opened:
    command = input().upper()
    print(commands.get(command, 'That is not a valid command, please try again.'))
    if command == 'MENU':
        menu_opened = True
        break
while not at_checkout and menu_opened:
    command1 = input().upper()
    if command1 == 'MENU':
        print('Menu is already open.')
    elif command1 == 'CANCEL':
        items.clear()
        print('Your order has been cancelled.')
    elif command1 == 'PROCEED':
        at_checkout = True
        print(at_checkout)
    elif menu_items.get(command1, 'That is not an item on the menu, please try again.') ==\
            'That is not an item on the menu, please try again.':
        print('That is not an item on the menu, please try again.')
    else:
        if menu_items.get(command1).has_options:
            menu_items.get(command1).display_options()
        else:
            name = menu_items.get(command1)
            print(f'{name.name} has been added to shopping cart')
        items.append((menu_items.get(command1)))


else:
    for item in items:
        checkout += f' {items.count(item)} {item.name}'
        for number in range(items.count(item)):
            items.remove(item)
            subtotal += round(item.price, 2)
round(subtotal, 2)
print(checkout)
tax = round(subtotal * 0.13, 2)
total = round(subtotal + tax, 2)
print(f'Your subtotal is: ${subtotal}')
print(f'Your tax is: ${tax}')
print(f'Your total is: ${total}')
print('Type "PURCHASE" to complete the purchase: ')
while at_checkout and not purchase_complete:
    confirmation = input().upper()
    if confirmation == 'PURCHASE':
        print('Items bought successfully, enjoy your meal!')
        purchase_complete = True
    elif confirmation == 'CANCEL':
        print('Your order has been cancelled.')
        at_checkout = False
    else:
        print('That is not a valid command, please try again.')
