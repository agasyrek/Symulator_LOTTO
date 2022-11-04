import random


def enter_num():
    """Get number from user
    :rtype int
    :return list of given numbers"""
    n = 0
    list_of_num = []
    while n < 6:
        entered_num = input("Enter number from 1 to 49 ")
        try:
            entered_num = int(entered_num)
            if entered_num in list_of_num:
                print("You have already entered this number, please enter a different one")
            elif (entered_num < 1 or entered_num > 49):
                print("You entered a number outside the range, enter a number between 1 and 49")
            else:
                list_of_num.append(entered_num)
                n = n + 1
        except ValueError:
            print("The value entered is not a number")
    list_of_num.sort()
    print(f"Entered numbers: {list_of_num}")
    return list_of_num


def draw_num():
    """The function draws 6 numbers from 1 to 49
    :rtype int
    :return list of drawn numbers"""
    lotto_list = []
    for i in range(0, 6):
        draw_num = random.randint(1, 49)
        lotto_list.append(draw_num)
    print(f"Drawn numbers: {lotto_list}")
    return lotto_list


def lotto():
    """The function checks how many of the numbers entered by the user
    have been randomly selected by the computer
    :rtype int
    return number of hit numbers"""
    list_of_num = enter_num()
    lotto_list = draw_num()
    hit = 0
    for number in list_of_num:
        if number in lotto_list:
            hit = hit + 1
    if hit == 0:
        print("you didn't hit any number")
    elif hit == 1:
        print(f"You hit {hit} number")
    else:
        print(f"You hit {hit} numbers")


lotto()
