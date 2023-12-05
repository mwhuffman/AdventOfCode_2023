#!/usr/bin/python

import os, sys, re

file = "day_02.txt"
records = open(file, 'r', encoding='utf-8')

sum_power_set = 0

for record in records:

    game_power_set = 1
    max_red   = 0
    max_green = 0
    max_blue  = 0
    (game_id_str, rounds) = record.split(":")

    game_id = re.search(r'\d+', game_id_str)
    game_id = int(game_id.group(0))
    print("game: " + str(game_id))

    rounds = re.sub(r'\n', '', rounds)
    all_rounds = rounds.split(";")

    for the_round in all_rounds:
        num_red = num_green = num_blue = 0
        # print(my_round)
        cubes = the_round.split(',')
        for the_cubes in cubes:
            the_cubes = re.sub(r'^ ', '', the_cubes)
            # print(the_cubes)
            (amount, color) = the_cubes.split(" ")
            match color:
                case "red":
                    if ( int(amount) > max_red ):
                        max_red = int(amount)
                case "green":
                    if (int(amount) > max_green):
                        max_green = int(amount)
                case "blue":
                    if (int(amount) > max_blue):
                        max_blue = int(amount)
            print(" > red: " + str(max_red) + " green: " + str(max_green) + " blue: " + str(max_blue))
    game_power_set = max_red * max_green * max_blue
    print("game power set total: " + str(game_power_set))
    sum_power_set += game_power_set
    
print("power set total: " + str(sum_power_set))
