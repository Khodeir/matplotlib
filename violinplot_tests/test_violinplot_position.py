from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy.random import normal
import traceback


data = [[10, 1, 10, 1, 10, 10, 10, 10],
                [10, 9, 8, 7, 6, 5, 4, 3],
                [1,1],
                [1, 2],
                [0, 10],
                [0, 5, 5, 5, 5, 5, 10],
                [0, 5, 5, 2, 5, 5, 10],
                [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 7, 7, 7, 7, 11], [-1,0,1]]


def reference_plot():
    fig = figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.violinplot(data)
    return ax2

# Redundant position argument 
def redundant_pos_arg():
    ax2 = reference_plot()
    ax2.violinplot(data, positions=range(1,len(data)+1))
    show()

# Reversed plot
def reverse_pos_arg():
    ax2 = reference_plot()
    ax2.violinplot(data, positions=range(1,len(data)+1)[::-1])
    show()

# Swapped first and third positions plot
def swap13_pos_arg():
    ax2 = reference_plot()
    pos = range(1, len(data) + 1)
    pos[0], pos[2] = pos[2], pos[0]
    ax2.violinplot(data, positions=pos)
    show()

if __name__ == '__main__':


    try:
        print 'TEST 1: Specified positions same as default (i.e. range(1, n+1))'
        print 'Manual Check that the right plot matches the left plot.'
        redundant_pos_arg()
        print 'TEST 1 RAN SUCCESSFULLY'
    except Exception:
        print 'FAIL: Something went wrong while plotting with positions=range(1,len(data)+1)'

    try:
        print 'TEST 2: Specified positions reversed (i.e. range(1,n+1)[::-1])'
        print 'Manual Check that the right plot is the same as the left one in reverse'
        reverse_pos_arg()
        print 'TEST 2 RAN SUCCESSFULLY'
    except Exception:
        print 'FAIL: Something went wrong while plotting with postions=range(1,len(data)+1)[::-1]'

    try:
        print 'TEST 3: Swap positions 1 and 3'
        print 'Manual Check that the "violins" at 1st and 3rd positions have been swapped. 1st violin should be empty space.'
        swap13_pos_arg()
        print 'TEST 3 RAN SUCCESSFULLY'
    except Exception:
        print 'FAIL: Something went wrong while plotting positions 1 and 3 swapped.'

