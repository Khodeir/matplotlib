from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy.random import normal


# Creating tests for colors

# test when no vert arg is passed, it should default to vertical
def test_vertical_orientation():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax = fig.add_subplot(111)
        ax.violinplot(data)
        show()

# test when vert is set to false for horizontal spanning violins
def test_horizontal_orientation():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax = fig.add_subplot(111)
        ax.violinplot(data, vert=False)
        show()



if __name__=="__main__":

    print 'Running Test #1: Default vertical orientation'
    try:
        print '    Manual check that violins are vertical'
        test_vertical_orientation()
        print '    Success: Test #1 Passed (it build and displayed)'
    except ValueError:
        print '    Failure: Test #1 Failed to run'


    print 'Running Test #2: horizontal orientation with horizontal violins '
    try:
        print '    Manual check that violins are displayed horizontally and x and y ticks swapped'
        test_horizontal_orientation()
        print '    Success: Test #2 Passed (it build and displayed)'
    except ValueError:
        print '    Failure: Test #2 Failed to run'


