from edit_distance import *


def debug_edit_distance():
    s='shorts'
    t='ports'
    diff=edit_distance(s,t)
    print(diff)


if __name__=='__main__':
    debug_edit_distance()