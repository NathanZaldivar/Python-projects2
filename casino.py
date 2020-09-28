import random
import time

person = str(input('name:'))
amount = int(input('Money:'))

class Gambler:
    def __init__(self, name, money):
        self.money = money
        self.name = name

gambler = Gambler(person, amount)

class Casino:
    def __init__(self, fool):
        self.fool = fool
        self.name = self.fool.name
    def pick_a_game(self):
        if self.fool.money <= 0:
            print('YOU GOT NO MONEY FOOL, GET OUT!\nGAME OVER')
            quit()
        print('what game would you like to play {name}?\ngames:\nflip a coin\ncho han\nquit(quits the game)'.format(name=self.name))
        game = input()
        if game == 'flip a coin':
            self.coin()
        elif game == 'cho han':
            self.Cho_Han()
        elif game == 'quit':
            quit()
        else:
            print('invalid game')
            self.pick_a_game()
    def coin(self):
        pick = input("heads or tails?\n")
        bet = int(input('How much of a bet?\n'))
        choices = ['heads', 'tails']
        count = 0
        for i in choices:
            if pick == i:
                count += 1
        if bet > self.fool.money:
            print('You bet more Than you have! What are you trying to pull?')
            self.coin()
        if count == 0:
            print('invalid input, choose heads or tails')
            self.coin()
        if pick == random.choice(choices):
            print('Congrats you won {amount}$\n'.format(amount=bet))
            self.fool.money += bet
        else:
            print('sad times you lost {amount}\n'.format(amount=bet))
            self.fool.money = self.fool.money - bet
        print('you now have {amount}$'.format(amount=self.fool.money))
        print('\nLoading next game...\n')
        time.sleep(3)
        self.pick_a_game()
    def Cho_Han(self):
        rolls = [1, 2, 3, 4, 5, 6]
        choices = ['even', 'odd']
        choice = input('will the dice roll even or odd?')
        count = 0
        for i in choices:
            if choice == i:
                count += 1
        if count == 0:
            print('you much choose either even or odd')
            self.Cho_Han()
        bet = int(input('How much will you bet?'))
        if bet > self.fool.money:
            print('Hey thats more than you have, you trying to cheat?')
            self.Cho_Han()
        roll1 = random.choice(rolls)
        roll2 = random.choice(rolls)
        sum = roll1 + roll2
        print('Rolling...')
        time.sleep(3)
        print('dice1 rolled {amount}'.format(amount=roll1))
        time.sleep(1)
        print('dice2 rolled {amount}'.format(amount=roll2))
        time.sleep(1)
        print('Total is {amount}'.format(amount=sum))
        time.sleep(1)
        if sum % 2 == 0:
            if choice == 'even':
                print('You won {amount}$'.format(amount=bet))
                self.fool.money += bet
            else:
                print('You lost {amount}$'.format(amount=bet))
                self.fool.money = self.fool.money - bet
        elif sum % 2 != 0:
            if choice == 'odd':
                print('You won {amount}$'.format(amount=bet))
                self.fool.money += bet
            else:
                print('You lost {amount}$'.format(amount=bet))
                self.fool.money = self.fool.money - bet
        print('\nyou now have {amount}$\n'.format(amount=self.fool.money))
        self.pick_a_game()
Gambino = Casino(gambler)
Gambino.pick_a_game()
