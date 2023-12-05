#!/usr/bin/python

import os, sys, re

#########
#
#

def intersection( list1, list2):

    list3 = [value for value in list1 if value in list2]

    return list3


#########
#
#

def normalize_array(num_array):

    while ("" in num_array):
        num_array.remove("")

    num_array.sort(key=int)
    num_array = sorted([int(x) for x in num_array])
    
    return(num_array)


#########
#
#

def main():

    file      = "day_04.txt"
    records   = open(file, "r")
    total_pts = 0
    sum_pts   = 0

    for record in records:
        record = record.replace("\n", "")

        (card_num, card) = record.split(":")
        (card_win, card_nums) = card.split("|")

        # winning numbers
        win_nums_array = normalize_array(card_win.split(" "))

        # card numbers
        card_nums_array = normalize_array(card_nums.split(" "))
    
        match_array = intersection(win_nums_array, card_nums_array)

        if (len(match_array) >= 1):
            sum_pts = 1
            for i in range(1, len(match_array)):
                sum_pts *= 2

        print("match array: " + str(match_array) + " len: " + str(len(match_array)) + " points: " + str(sum_pts))

        total_pts += sum_pts

    print("total points: " + str(total_pts))

    
#########
#
#

if __name__ == "__main__":
    main()
