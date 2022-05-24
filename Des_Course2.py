import pyautogui as pag
import time as t
import random


def the_gui():
    limit = 10
    msg = input("unajaribu kusema nini? \n")
    i = 0
    t.sleep(2)
    for i in range(limit):
        t.sleep(0.5)
        pag.typewrite(msg)
        pag.press('Enter')
        # message is printed in a natural way until last iteration in the for loop!
    i += 1


the_gui()


def the_sum():
    x = 0
    while x < 20:
        x = x + 3
    print(x)


def tuple_list_pop():
    lst = [(0, [2, 3, 4]), ([6, 7, 8], 0)]
    lst1 = [g for g in lst if g[0] == 0]
    lst2 = [t for t in lst if t[0] != 0]
    print(lst1)
    print(lst2)


def median(nums1: list[int], nums2: list[int]) -> float:
    answer_list = nums1 + nums2
    answer_list.sort()
    length: int = len(answer_list)
    if (length % 2) == 0:
        x = int(length / 2)
        y = int((length / 2) - 1)
        return (answer_list[x] + answer_list[y]) / 2
    elif length % 2:
        x = int(length / 2)
        return answer_list[x]


class Solution:
    # the pass function returns None values in the class!
    pass


solution = Solution()
print(median([1, 2, 3], [3, 2, 1]))


def ret_even():
    ls1 = [1, 6, 7, 8, 9, 3, 4, 5, 10, 2]
    lst2 = []
    for c in ls1:
        if c % 2 != 0:
            print(f"this be the even numbers in list: {c}")
            lst2.append(c)
            print(lst2)


ret_even()


def reading():
    nodesName = 'rtr03'
    try:
        with open("nodes.txt", "r+") as f:

            if nodesName in f.readlines():
                print('Duplicate in the List!')

            else:
                with open("nodes.txt", "r+") as f:

                    if nodesName in f.read():
                        print('Duplicate in the String!')
    except:
        pass


def the_payer():
    names = ['destinne', 'agugu', 'trinity', 'amy', 'maria']
    num_items = len(names)
    random_choice = random.randint(0, num_items - 1)
    # Pick out random person from list of names using the random number.
    person_who_will_pay = names[random_choice]
    # Also, can be replaced by person_who_will_pay = random.choice(names)

    print(person_who_will_pay + " ndo anatununulia kachai leo!")


the_payer()
