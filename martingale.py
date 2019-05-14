import random
#
import time

import matplotlib.pyplot as plt


def rollDice():
    roll = random.randint(1, 100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


def doubler_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentwager = 1

    # since we'll be betting based on previous bet outcome #
    previouswager = 'win'

    # since we'll be doubling #
    previouswageramount = initial_wager

    while currentwager <= wager_count:
        if previouswager == 'win':
            print('we won the last wager, yay!')
            if rollDice():
                value += wager
                print(value)
                wX.append(currentwager)
                vY.append(value)
            else:
                value -= wager
                previouswager = 'loss'
                print(value)
                previouswageramount = wager
                wX.append(currentwager)
                vY.append(value)
                if value < 0:
                    print('went broke after', currentwager, 'bets')
                    currentwager += 10000000000000000
        elif previouswager == 'loss':
            print('we lost the last one, so we will be super smart & double up!')
            if rollDice():
                wager = previouswageramount * 2
                print('we won', wager)
                value += wager
                print(value)
                wager = initial_wager
                previouswager = 'win'
                wX.append(currentwager)
                vY.append(value)
            else:
                wager = previouswageramount * 2
                print('we lost', wager)
                value -= wager
                if value < 0:
                    print('went broke after', currentwager, 'bets')
                    currentwager += 10000000000000000
                print(value)
                previouswager = 'loss'
                previouswageramount = wager
                wX.append(currentwager)
                vY.append(value)
                if value < 0:
                    print('went broke after', currentwager, 'bets')
                    currentwager += 10000000000000000

        currentwager += 1

    print(value)
    plt.plot(wX, vY)


doubler_bettor(10000, 100, 100)
plt.show()
time.sleep(555)


'''
Simple bettor, betting the same amount each time.
'''


def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentwager = 1
    while currentwager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentwager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentwager)
            vY.append(value)
        currentwager += 1
    plt.plot(wX, vY)


x = 0


while x < 100:
    simple_bettor(10000, 100, 1000)
    x += 1

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
