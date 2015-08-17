#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################
def reverse_lookup_old(d, v):
	for k in d:
		if d[k] == v:
			return k
	raise ValueError

def reverse_lookup_new(d, v):
	list_ = []
	for k in d:
		if d[k] == v:
			list_.append(k)
	return list_
	# raise ValueError


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
def main():   # DO NOT CHANGE BELOW
	pledge_histogram = histogram_new(get_pledge_list())
	print reverse_lookup_new(pledge_histogram, 1)
	print reverse_lookup_new(pledge_histogram, 9)
	print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()
