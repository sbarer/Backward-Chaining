#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:59:27 2018

@author: simonbarer
"""
import sys

### SOLVE FUNCTION ###
def solve(goals):
    # if the list entry is empty, function reached a fact
    if len(goals[0]) == 0:
        print('ARRIVED AT FACT')
        # pop empty element from goals
        goals.pop(0)
        return True
    target = goals.pop(0)

    # boolean to account for multiple atoms in a rule
    check = False

    # parse each atom in the rule, target
    for j in target:
        # progress through each rule in kb
        for r in range(0, len(kb)):
            # if the target query matches a rule in kb
            #print("querying rule %s" % kb[r][0])
            if kb[r][0] == j:
                print("Evaluating '%s'" % j)
                print('\t\tFound rule %s in kb' % kb[r])
                print('\t\t\tAppending Atom(s) %s to Goals' % kb[r][1:])
                # insert that atom's corresponding rule into the goals list, a rule will append [] (empty element)
                goals.insert(0, kb[r][1:])
                # bool ensures compound rules are accounted for
                if solve(goals) is True:
                    # atom is True
                    print('\tTherefore:')
                    print('\t\t[%s] is TRUE' % j)
                    if j is target[len(target)-1] and len(target) > 1:
                        # Compound Rule is True
                        print('\tTherefore:')
                        print('\t\t%s is TRUE' % target)
                    check = True
                else:
                    check = False
        # break for loop if any atom in compound rule is found to be false
        if check is False:
            print('\t%s IS FALSE' % target)
            return False

    # will return True iff all atoms in the given rule are true, otherwise returns false
    return True




### START OF PROGRAM ###

# print description of program
print("You have entered a program that checks the validity of queries through Backward Chaining.\n\tPlease type 'quit' if you wish to terminate.\n")

# read file from command line, store in program
#file = "test2.txt"
#file = "310assn2test.txt"
file = sys.argv[1]

# Initialize kb list
kb = []
# Populate kb with rules from input file
if file:
    with open(file, 'r') as f:
        for index, line in enumerate(f):
            # remove extraneous characters
            line = line.strip().replace('[', '').replace(']', '').replace(',', ' ').replace('\\', ' ').replace('}', ' ').split()
            kb.append(line)

# Loop for user inputs until program terminated
while True:
    # request query
    q = input("Please enter a single query: ")
    # exit clause to quit program
    if q == 'quit':
        exit(0)
    elif len(q) > 1:
        print("Error: Invalid query.")
        continue

    #print(kb)
    # cast q to lower case to ensure query is well formed
    q = q.lower()
    # call solving function
    print()
    answer = solve([q])

    # print answer
    print("By Backward Chaining, it's been found that:\n\n\tQuery '%s' is %s\n" % (q, answer))
