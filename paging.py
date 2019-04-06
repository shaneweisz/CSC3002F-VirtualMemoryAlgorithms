# Shane Weisz
# WSZSHA001

import sys
from random import randint


def FIFO(size, pages):
    """
    Function that implements the FIFO page replacement algorithm and
    returns the number of page faults that occur.

    Parameters:
        size (int): The number of available page frames - can vary from 1 to 7
        pages (list): A page reference string e.g. [1, 2, 3, 5, 1, 2, 3, 5]

    Returns:
        int: The number of page faults that occured.
    """

    queue = []                   # queue, the page frames, is initially empty
    page_faults = 0              # tracks the number of page faults

    for page in pages:           # loops through each page in the page ref str
        if page not in queue:    # check if the page is in memory already
            page_faults += 1         # if not, a page fault has occurred
            if len(queue) >= size:   # check if there are no empty frames left
                del queue[0]            # if full, remove page at head of queue
            queue.append(page)   # append the new page at end of queue

    return page_faults


def LRU(size, pages):
    """
    Function that implements the LRU (Least Recently Used) page replacement
    algorithm and returns the number of page faults that occur.

    Parameters:
        size (int): The number of available page frames - can vary from 1 to 7
        pages (list): A page reference string e.g. [1, 2, 3, 5, 1, 2, 3, 5]

    Returns:
        int: The number of page faults that occured.
    """

    stack = []                   # stack, the page frames, is initially empty
    page_faults = 0              # tracks the number of page faults

    for page in pages:           # loops through each page in the page ref str
        if page not in stack:    # check if the page is in memory already
            page_faults += 1        # if not, a page fault has occurred
            if len(stack) >= size:  # check if there are no empty frames left
                del stack[size-1]       # remove the least recently used page
        else:                    # page is in memory
            stack.remove(page)      # remove page from old place in stack
        # put page on top of the stack because its the most recently used page.
        stack.insert(0, page)

    return page_faults


def OPT(size, pages):
    """
    Function that implements the optimal page replacement algorithm (OPT)
    and returns the number of page faults that occur.

    Parameters:
        size (int): The number of available page frames - can vary from 1 to 7
        pages (list): A page reference string e.g. [1, 2, 3, 5, 1, 2, 3, 5]

    Returns:
        int: The number of page faults that occured.
    """

    frames = []                  # represent the frames in physical memory
    page_faults = 0              # tracks the number of page faults

    for (page_index, page) in enumerate(pages):  # loop through page ref string
        if page not in frames:        # check if the page is in memory already
            page_faults += 1            # if not, a page fault has occurred
            if len(frames) < size:    # check if there are any free frames
                frames.append(page)     # if so, place page in a free frame
            else:
                # the frames are full, so we must replace the frame
                # that will not be used for the longest period of time

                frame_to_replace = frames[0]        # initialize to first frame
                max_time_till_use = 0               # initialize to zero
                upcoming_pages = pages[page_index+1:]

                # loop through frames in memory to find the frame to replace
                for frame in frames:
                    # check if the frame will not be used in the near future
                    # if so, we can replace this frame
                    if frame not in upcoming_pages:
                        frame_to_replace = frame
                        break

                    # find the next usage and time until the frame is next used
                    for (i, upcoming_page) in enumerate(upcoming_pages, 1):
                        if frame == upcoming_page:
                            time_till_use = i
                            break

                    # check if this frame has the current longest time till use
                    if time_till_use > max_time_till_use:
                        max_time_till_use = time_till_use
                        frame_to_replace = frame

                # replace the chosen frame with the new page
                pos = frames.index(frame_to_replace)
                frames.remove(frame_to_replace)
                frames.insert(pos, page)

    return page_faults


def generate_page_reference_string(N):
    """
    Generates a random page-reference string of length N
    where page numbers range from 0 to 9

    Parameters:
        N (int): The desired length of the page reference string

    Returns:
        list: a list of page references e.g. [0,2,4,1,2,3]
    """

    pages = []                          # Stores the page-reference string
    for i in range(N):
        pages.append(randint(0, 9))     # Generates a random number from [0,9]
    return pages


def main():
    """
    A randomly generated page-reference string is applied to each of the FIFO,
    LRU and optimal page replacement algorithms, and the number of page faults
    incurred by each algorithm is recorded.
    """

    # N = int(input("Enter the length of the page reference string: "))
    # generate_page_reference_string(N)

    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    # pages = [8, 5, 6, 2, 5, 3, 5, 4, 2, 3, 5, 3, 2, 6, 2, 5,
    #          6, 8, 5, 6, 2, 3, 4, 2, 1, 3, 7, 5, 4, 3, 1, 5]
    # pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

    size = int(sys.argv[1])  # number of pages
    print "FIFO", FIFO(size, pages), "page faults."
    print "LRU", LRU(size, pages), "page faults."
    print "OPT", OPT(size, pages), "page faults."


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python paging.py [number of pages]"
    else:
        main()
