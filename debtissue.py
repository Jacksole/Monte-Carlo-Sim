import random

import matplotlib.pyplot as plt

samplesize = 100

startingfunds = 10000
wagersize = 100
wagercount = 1000


def rolldice():
    roll = random.randint(1, 100)
    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


# edit in color


def doubler_bettor(funds, initial_wager, wager_count, color):
    value = funds
    wager = initial_wager
    wx = []
    vy = []
    currentwager = 1
    previouswager = 'win'
    previouswageramount = initial_wager

    while currentwager <= wager_count:
        if previouswager == 'win':
            if rolldice():
                value += wager
                wx.append(currentwager)
                vy.append(value)
            else:
                value -= wager
                previouswager = 'loss'
                previouswageramount = wager
                wx.append(currentwager)
                vy.append(value)
                if value < 0:
                    currentwager += 10000000000000000
        elif previouswager == 'loss':
            if rolldice():
                wager = previouswageramount * 2

                # this makes it so we just bet all that is left.
                if (value - wager) < 0:
                    wager = value

                value += wager
                wager = initial_wager
                previouswager = 'win'
                wx.append(currentwager)
                vy.append(value)
            else:
                wager = previouswageramount * 2
                # this makes it so we just bet all that is left.
                if (value - wager) < 0:
                    wager = value
                value -= wager
                previouswager = 'loss'
                previouswageramount = wager
                wx.append(currentwager)
                vy.append(value)

                # change to equals zero!
                if value <= 0:
                    currentwager += 10000000000000000

        currentwager += 1
    # this guy edits color #
    plt.plot(wx, vy, color)


'''
Simple bettor, betting the same amount each time.
'''


# color #


def simple_bettor(funds, initial_wager, wager_count, color):
    value = funds
    wager = initial_wager
    wx = []
    vy = []
    currentwager = 1
    while currentwager <= wager_count:
        if rolldice():
            value += wager
            wx.append(currentwager)
            vy.append(value)
        else:
            value -= wager
            wx.append(currentwager)
            vy.append(value)

            # change this part, not less than or equal zero, it is zero
            if value <= 0:
                currentwager += 10000000000000000
        currentwager += 1

    # this guy goes green #
    plt.plot(wx, vy, color)


x = 0

while x < samplesize:
    simple_bettor(startingfunds, wagersize, wagercount, 'c')
    # simple_bettor(startingFunds,wagerSize*2,wagerCount,'c')
    doubler_bettor(startingfunds, wagersize, wagercount, 'k')
    x += 1

plt.axhline(0, color='r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
