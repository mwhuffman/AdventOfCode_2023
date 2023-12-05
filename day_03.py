#!/usr/bin/python

import os, sys, re

##########
#
#
#

def parse_num(line):

    # print("Line: " + line )

    num_str = ""

    for k in range(0, len(line)):
        
        if ( line[k].isnumeric() ):
            num_str += line[k]
        else:
            return (num_str, k)

    # print(" >> num: " + num_str + " k: " + str(len(line)))
    return (num_str, len(line))
        
##########
#
#
#

def parse_line( prev_line, line, next_line):

    # DEBUG:
    if prev_line != "":
        print("Prev: " + prev_line)
    print("Line: " + line)
    orig_line = line
    if next_line != "":
        print("Next: " + next_line)

    sum = 0
    j = 0
    
    while (j < len(line)):
        
        k = 0
        num_str = ""

        if ( line[j].isnumeric() ):
            (num_str, k) = parse_num(line[j:])
            
            if ( num_str != "" ):
                if ( int(num_str) > 0 ):
                    print("num: " + num_str + " j: " + str(j) + " k: " + str(k))
                    sum += is_part(prev_line, orig_line, next_line, num_str, j, k)
                    j += k
                    # print("sum: " + str(sum) + "\n")
                    
        else:
            j+= 1
        
               
    return sum


##########
#
#
#

def is_part(prev_line, orig_line, next_line, num_str, j, k):

    if ( j == 0 ):
        prev_str = prev_line[j:(j+k+1)]
        orig_str = orig_line[j:(j+k+1)]
        next_str = next_line[j:(j+k+1)]
    else:
        prev_str = prev_line[(j-1):(j+k+1)]
        orig_str = orig_line[(j-1):(j+k+1)]
        next_str = next_line[(j-1):(j+k+1)]

    print("prev: " + prev_str)
    print("orig: " + orig_str)
    print("next: " + next_str)

    prev_str = re.sub(r'\.', '', prev_str)
    orig_str = re.sub(r'\.', '', orig_str)
    next_str = re.sub(r'\.', '', next_str)

    # print("prev: " + prev_str)
    # print("orig: " + orig_str)
    # print("next: " + next_str)

    if ( (prev_str == "") and (next_str == "") ):
        if ( num_str == orig_str ):
            print(" > not engine part")
            return(0)
        else:
            print(" > " + num_str)
            return(int(num_str))
    else:
        print(" > " + num_str)
        return(int(num_str))
    

    

##########
#
#
#

def main():
    
    file = "day_03.txt"
    sum_part_nums = 0
    records = {}
    
    i = 0
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            line = re.sub(r'\n', '', line)
            records[i] = line
            i += 1

    num_records = len(records)
    print("len: " + str(num_records))

    for i in range(num_records):
    
        prev_line = ""
        line = ""
        next_line = ""
    
        if ( i >= 1 ):
            prev_line = records[(i - 1)]
            line = records[i]
        if ( i < num_records - 1):
            next_line = records[(i + 1)]

        if line != "":
            sum_part_nums += parse_line(prev_line, line, next_line)

        # print("\n")
    
    print("total: " + str(sum_part_nums))

#########
#
#

if __name__ == "__main__":
    main()
