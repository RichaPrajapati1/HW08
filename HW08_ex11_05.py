#!/usr/bin/env python
# Exercise 5
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Update print_hist_new from HW08_ex_11_03.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
##############################################################################

def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val,[])
        inverse[val].append(key)
    return inverse


def print_hist_newest(d):
    # list_ = d.keys()
    # list_ = sorted(list_)
    for i in range(1,max(d,key = int)+1):
        if i in d:
            print "'"+str(i)+":"+str(d[i])+"'"
        else:
            print "'"+str(i)+":"+"'"
        

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################

def histogram_new(s):
    d = {}
    for c in s:
        d[c] = d.get(c,0) + 1
    return d


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    with open("pledge.txt") as fin:
        words = fin.read()
        words = words.replace(':','').replace('.','').replace(',','').lower()
        pledge_list = words.split()
    return pledge_list


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
