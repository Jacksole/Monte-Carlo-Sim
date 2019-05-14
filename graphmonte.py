import random
import matplotlib
import matplotlib.pyplot as plt
import time



samplesize = 1000

startingfunds = 10000
wagersize = 1000
wagercount = 10000




def rolldice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


def doubler_bettor(funds,initial_wager,wager_count):

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

        currentwager += 1
    # this guy goes cyan #
    plt.plot(wX,vY,'c')

#####                                           color#
def simple_bettor(funds,initial_wager,wager_count,color):
    ####

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

            ###add me
            if value < 0:
                currentwager += 10000000000000000
        currentwager += 1

    # this guy goes green #
    plt.plot(wX,vY,color)


x = 0

while x < sampleSize:
    simple_bettor(startingfunds,wagersize,wagercount,'k')
    simple_bettor(startingfunds,wagersize*2,wagercount,'c')
    #doubler_bettor(startingFunds,wagerSize,wagerCount)
    x+=1

plt.axhline(0, color = 'r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
	
