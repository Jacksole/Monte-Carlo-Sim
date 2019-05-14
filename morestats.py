import random

import matplotlib.pyplot as plt


def rolldice():
    roll = random.randint(1, 100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


def doubler_bettor(funds, initial_wager, wager_count):
    global broke_count
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentwager = 1
    previouswager = 'win'
    previouswageramount = initial_wager

    while currentwager <= wager_count:
        if previouswager == 'win':
            if rolldice():
                value += wager
                wX.append(currentwager)
                vY.append(value)
            else:
                value -= wager
                previouswager = 'loss'
                previouswageramount = wager
                wX.append(currentwager)
                vY.append(value)
                if value < 0:
                    broke_count += 1
                    currentwager += 10000000000000000
        elif previouswager == 'loss':
            if rolldice():
                wager = previouswageramount * 2
                value += wager
                wager = initial_wager
                previouswager = 'win'
                wX.append(currentwager)
                vY.append(value)
            else:
                wager = previouswageramount * 2
                value -= wager
                previouswager = 'loss'
                previouswageramount = wager
                wX.append(currentwager)
                vY.append(value)
                if value < 0:
                    currentwager += 10000000000000000
                    broke_count += 1

        currentwager += 1

    plt.plot(wX, vY)


def simple_bettor(funds, initial_wager, wager_count):
    ####
    global broke_count

    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentwager = 1
    while currentwager <= wager_count:
        if rolldice():
            value += wager
            wX.append(currentwager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentwager)
            vY.append(value)

            # add me
            if value < 0:
                currentwager += 10000000000000000
                broke_count += 1
        currentwager += 1
    plt.plot(wX, vY)


x = 0
broke_count = 0
while x < 1000:
    simple_bettor(10000, 100, 1000)
    x += 1
print(('death rate:', (broke_count / float(x)) * 100))
print(('survival rate:', 100 - ((broke_count / float(x)) * 100)))
plt.axhline(0, color='r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
