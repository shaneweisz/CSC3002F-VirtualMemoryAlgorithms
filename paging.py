# Shane Weisz
# WSZSHA001

import sys
from random import randint


def FIFO(size, pages):
    # size = number of pages/frames
    # pages = page reference string
    # returns the number of faults using FIFO

    queue = []                   # queue is initially empty
    page_faults = 0              # tracks the number of page faults

    for page in pages:           # loop through each page in the page ref str
        if page not in queue:
            page_faults += 1     # a page fault has occurred
            del queue[0]         # remove page at head of queue
            queue.append(page)   # append the new page at end of queue

    return page_faults


def LRU(size, pages):
    # size = number of pages
    pass


def OPT(size, pages):
    # size = number of pages
    pass


def main():
    # Generates a random page-reference string where page nos range from 0 to 9
    pages = []                           # The page-reference string itself
    for i in range(20):                  # Assume 20 pages in pag
        pages.append(randint(0, 9))      # Generates a random number from [0,9]

    # pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    print pages

    # Apply the random page-reference string to each algorithm,
    # and record the number of page faults incurred by each algorithm.
    size = int(sys.argv[1])  # number of pages
    print "FIFO", FIFO(size, pages), "page faults."
    print "LRU", LRU(size, pages), "page faults."
    print "OPT", OPT(size, pages), "page faults."


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python paging.py [number of pages]"
    else:
        main()
