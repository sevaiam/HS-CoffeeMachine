# Write your code here

class CoffeeMachine:

    def __init__(self):
        self.has_water = 400
        self.has_milk = 540
        self.has_beans = 120
        self.has_cups = 9
        self.has_money = 550
        self.state = 'menu'

    def fill(self):
        self.has_water += int(input('Write how many ml of water you want to add: '))
        self.has_milk += int(input('Write how many ml of milk you want to add: '))
        self.has_beans += int(input('Write how many grams of coffee beans you want to add: '))
        self.has_cups += int(input('Write how many disposable cups of coffee you want to add: '))

    def take(self):
        print(f'I gave you ${self.has_money}')
        self.has_money = 0

    def printout(self):
        print('The coffee machine has:')
        print(f'{self.has_water} ml of water\n'
              f'{self.has_milk} ml of milk\n'
              f'{self.has_beans} g of coffee beans\n'
              f'{self.has_cups} disposable cups\n'
              f'${self.has_money} of money')

    def make_coffee(self, numb):
        numb = int(numb)

        if numb == 1:
            need_water = 250
            need_beans = 16
            need_cups = 1
            need_money = 4
            need_milk = 0
        elif numb == 2:
            need_water = 350
            need_milk = 75
            need_beans = 20
            need_cups = 1
            need_money = 7
        elif numb == 3:
            need_water = 200
            need_milk = 100
            need_beans = 12
            need_cups = 1
            need_money = 6

        if self.has_water < need_water:
            print('Sorry, not enough water!')
        elif self.has_milk < need_milk:
            print('Sorry, not enough milk!')
        elif self.has_beans < need_beans:
            print('Sorry, not enough coffee beans!')
        elif self.has_cups < need_cups:
            print('Sorry, not enough disposable cups!')
        else:
            print('I have enough resources, making you a coffee!')
            self.has_water -= need_water
            self.has_cups -= need_cups
            self.has_milk -= need_milk
            self.has_beans -= need_beans
            self.has_money += need_money


machine = ''
rocket = CoffeeMachine()
while machine != 'exit':
    machine = input('Write action (buy, fill, take, remaining, exit):')
    if machine == 'buy':
        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
        if coffee == 'back':
            pass
        else:
            rocket.make_coffee(coffee)

    elif machine == 'fill':
        rocket.fill()
    elif machine == 'take':
        rocket.take()
    elif machine == 'remaining':
        rocket.printout()
# want_cups = int(input('Write how many cups of coffee you will need:'))
#
# can_do_cups = has_beans // beans
# if has_water // water < can_do_cups:
#       can_do_cups = has_water // water
# if has_milk // milk < can_do_cups:
#       can_do_cups = has_milk // milk
#
# if want_cups == can_do_cups:
#       print('Yes, I can make that amount of coffee')
# elif want_cups < can_do_cups:
#       print(f'Yes, I can make that amount of coffee (and even {want_cups - can_do_cups} more than that)')
# else:
#       print(f'No, I can make only {can_do_cups} cups of coffee')
