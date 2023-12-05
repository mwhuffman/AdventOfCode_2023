#!/usr/bin/python

import os, sys, re

##########
#
#
#

def normalize_record( record ):

    record = re.sub(r'\n', '', record)
    print(record)
    
    record = re.sub(r'eighthree', '83', record)
    record = re.sub(r'eightwo', '82', record)
    record = re.sub(r'fiveight', '58', record)
    record = re.sub(r'nineight', '98', record)
    record = re.sub(r'oneight', '18', record)
    record = re.sub(r'twone', '21', record)
    record = re.sub(r'threeeight', '18', record)

    record = re.sub(r'five', '5', record)
    record = re.sub(r'four', '4', record)
    record = re.sub(r'nine', '9', record)
    record = re.sub(r'one', '1', record)
    record = re.sub(r'seven', '7', record)
    record = re.sub(r'six', '6', record)
    record = re.sub(r'three', '3', record)
    record = re.sub(r'two', '2', record)
    record = re.sub(r'eight', '8', record)
    print("record: " + record)
    
    record = re.sub(r'[a-zA-Z\n]+', '', record)
    print("record: " + record)
    
    return(record)
    
##########
#
#
#

def main():
    
    file = "day_01.txt"
    records = open(file, 'r', encoding='utf-8')

    sum = 0
    for record in records:

        left = 0
        right = 0

        record = normalize_record(record)
        
        left = re.search(r'^\d', record)
        # print("left: " + left.group(0))
    
        right = re.search(r'\d$', record)
        # print("right: " + right.group(0))

        coordinate = (int(left.group(0)) * 10) + int(right.group(0))
        
        print ("co: " + str(coordinate))

        sum += coordinate
    
        print("")
    
    records.close()

    print("total: " + str(sum))


#########
#
#

if __name__ == "__main__":
    main()
