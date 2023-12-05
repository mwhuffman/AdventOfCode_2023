#!/usr/bin/python

import os, sys, re

##########
#
#
#

def main():
    
    file = "day_02.txt"
    records = open(file, 'r', encoding='utf-8')
    game_total = 0

    # max
    max_red   = 12
    max_green = 13
    max_blue  = 14

    for record in records:

        game_score = 1
        (game_id_str, rounds) = record.split(":")

        game_id = re.search(r'\d+', game_id_str)
        game_id = int(game_id.group(0))
        print("game: " + str(game_id))

        rounds = re.sub(r'\n', '', rounds)
        all_rounds = rounds.split(";")

        for the_round in all_rounds:
            
            num_red = num_green = num_blue = 0
            cubes = the_round.split(',')

            for the_cubes in cubes:

                the_cubes = re.sub(r'^ ', '', the_cubes)
                (amount, color) = the_cubes.split(" ")
                
                match color:
                    case "red":
                        num_red = int(amount)
                    case "green":
                        num_green = int(amount)
                    case "blue":
                        num_blue = int(amount)
                    
            print(" > red: " + str(num_red) + " green: " + str(num_green) + " blue: " + str(num_blue))
            
            if ( (num_red > max_red) or (num_green > max_green) or (num_blue > max_blue) ):
                print(" > game not possible")
                game_score = 0

        if (game_score == 1):
            game_total += game_id

    print("game total: " + str(game_total))


#########
#
#

if __name__ == "__main__":
    main()
    
