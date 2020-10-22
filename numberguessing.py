import sys
import random

def go_to_game(min, max, numberLive, rNumber):
    ans = input("Please try your luck and guess the number that is between "+min+" and "+max+" : ")
    if (int(ans) == int(rNumber)):
        print("You've won GGS")
    else:
        if (int(numberLive) == 0):
            print("You lost, sorry :'(")
            exit(0)
        else:
            numberLive-=1
        print("Wrong answer, you lost one life. You have ",numberLive+1," life left")
        go_to_game(min, max, numberLive, rNumber)


def open_prompt():
    numberLive = 3
    rangeNumberMini = input("Enter minimum range : ")
    if (int(rangeNumberMini) > 0):
        rangeNumberMax = input("Enter maximum range : ")
        if (int(rangeNumberMax) > int(rangeNumberMini)):
            rNumber = random.randint(int(rangeNumberMini), int(rangeNumberMax))
            go_to_game(rangeNumberMini, rangeNumberMax, numberLive, rNumber)

def main():
    if (len(sys.argv) > 1):
        print("This mini game only launches without parameters")
        exit(0)
    else:
        open_prompt()


if __name__=="__main__":
    main()