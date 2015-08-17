#!/usr/bin/env python
# Exercise 3  
# Dictionaries have a method called keys that returns the keys of the 
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical 
# order.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
##############################################################################

def print_hist_old(h):
    for c in h:
        print c, h[c]


def print_hist_new(h):
    list_ = h.keys()
    list_ = sorted(list_)
    for word in list_:
    	print word, h[word]

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
##############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the 
    histogram of pledge.txt.
    """
    h = histogram_new(get_pledge_list())
    print_hist_new(h)
    

if __name__ == '__main__':
    main()
