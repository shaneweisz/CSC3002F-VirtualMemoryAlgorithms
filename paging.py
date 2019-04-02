import sys


def FIFO(size, pages):
    pass


def LRU(size, pages):
    pass


def OPT(size, pages):
    pass


def main():
    # ...TODO...
    pages = 0
    size = int(sys.argv[1])
    print "FIFO", FIFO(size, pages), "page faults."
    print "LRU", LRU(size, pages), "page faults."
    print "OPT", OPT(size, pages), "page faults."


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python paging.py [number of pages]"
    else:
        main()
