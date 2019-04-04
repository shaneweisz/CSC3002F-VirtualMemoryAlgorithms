# Shane Weisz
# WSZSHA001

import sys
from random import randint


# Function that returns the number of page faults using FIFO
def FIFO(size, pages):
    # size:  number of available frames - should be a value between 1 and 7
    # pages: page reference string

    queue = []                   # queue is initially empty
    page_faults = 0              # tracks the number of page faults

    for page in pages:           # loops through each page in the page ref str
        if len(queue) < size:    # check if the queue is full
            if page not in queue:
                page_faults += 1     # a page fault has occurred
                queue.append(page)   # append the new page at end of queue
        else:                    # the queue is now full
            if page not in queue:
                page_faults += 1     # a page fault has occurred
                del queue[0]         # remove page at head of queue
                queue.append(page)   # append the new page at end of queue

    return page_faults


# Function that returns the number of page faults using LRU
def LRU(size, pages):
    # size:  number of available frames - should be a value between 1 and 7
    # pages: page reference string

    stack = []                   # stack is initially empty
    page_faults = 0              # tracks the number of page faults

    for page in pages:           # loops through each page in the page ref str
        if len(stack) < size:    # check if the stack is full
            if page in stack:
                # remove page from old place in stack, to be inserted at head
                stack.remove(page)
            else:
                page_faults += 1    # page fault occurs since page not in stack
        else:                    # the stack is now full
            if page in stack:
                stack.remove(page)  # remove page from old place in the stack
            else:
                page_faults += 1    # page fault occurs since page not in stack
                del stack[size-1]   # remove the least recently used page
        # Put this page on top of stack because its most recently used
        stack.insert(0, page)

    return page_faults


# Function that returns the number of page faults using OPT
def OPT(size, pages):
    # size:  number of available frames
    # pages: page reference string - should be a value between 1 and 7

    page_faults = 0              # tracks the number of page faults
    frames = []                  # represent frames in physical memory

    for page in pages:           # loops through each page in the page ref str
        if len(frames) < size:   # check if there are any free frames
            if page not in frames:
                page_faults += 1      # a page fault has occurred
                frames.append(page)   # place the new page in a free frame
        else:
            if page not in frames:
                # we must replace the frame that will not be used for the
                # longest period of time
                frame_to_replace = frames[0]  # initialize to first frame
                max_time_till_use = 0
                upcoming_pages = pages  # upcoming pages to use
                for frame in frames:
                    pass

    return page_faults


def main():
    # Generates a random page-reference string where page nos range from 0 to 9
    N = int(input("Enter the size of the page reference string: "))
    pages = []                           # The page-reference string itself
    for i in range(N):                  # Assume 20 pages in page ref str
        pages.append(randint(0, 9))      # Generates a random number from [0,9]

    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    # pages = [8, 5, 6, 2, 5, 3, 5, 4, 2, 3, 5, 3, 2, 6, 2, 5]
    # pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

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
