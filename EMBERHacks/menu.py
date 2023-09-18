class Food:
    def __init__(self, price, name, has_options=False, number_of_options=0, option1='', option2='', option3='Nothing'):
        self.price = price
        self.has_options = has_options
        self.number_of_options = number_of_options
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.name = name

    def display_options(self):
        print('Which option would you like?')
        selection = (self.option1, self.option2, self.option3)
        for number in range(self.number_of_options):
            print(f'{number+ 1}: {selection[number]}')
        command2 = input()
        if command2 == '1':
            print(f'{self.name} ({self.option1}) has been added to shopping cart')
        elif command2 == '2':
            print(f'{self.name} ({self.option2}) has been added to shopping cart')
        elif command2 == '3':
            print(f'{self.name} ({self.option3}) has been added to shopping cart')
        else:
            print('That is not a valid option')
        while command2 == 0:
            command2 = input()
            if command2 == '1':
                print(f'{self.name} ({self.option1}) has been added to shopping cart')
            elif command2 == '2':
                print(f'{self.name} ({self.option2}) has been added to shopping cart')
            elif command2 == '3':
                print(f'{self.name} ({self.option3}) has been added to shopping cart')
            else:
                print('That is not a valid option')



hungry_marauder = Food(9.99, 'Hungry marauder')

pita_pocket = Food(6.50, 'Pita pocket', True, 3, 'Falafel', 'Chicken', 'Eggplant')

bridges_best = Food(11.50, 'Bridges best', True, 3, 'Wedges', 'Fries', 'Nothing')

teriyaki_chicken = Food(12.50, 'Teriyaki chicken')

hammertown_soups = Food(9.95, 'Hammertown soups', True, 3, 'Tofu', 'Grilled Chicken', 'Braised Beef')

onion_rings = Food(2.99, 'Onion rings', True, 3, 'Without a drink', 'With Sprite', 'With Water')

grilled_cheese = Food(3.99, 'Grilled cheese')
