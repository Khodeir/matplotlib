from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy.random import normal


# Creating tests for show/hide whiskers.

# test when no median arg is given.
def test_no_arg():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5)
        show()

# test when invalid (not none, line or point) arg given
def test_invalid_arg():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, median="banana")
        show()

# testing when median = line.
def test_line():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, median="line")
        show()

# testing when median = point.
def test_point():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, median="point")
        show()

# testing when median = none.
def test_no_median():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, median="none")
        show()


if __name__=="__main__":
# put tests here

    print 'Running Test #1: No arg'
    try:
        print '    Manual check that points are shown'
        test_no_arg()
        print '    Success: Test #1 Passed'
    except ValueError:
        print '    Failure: Test #1 Failed'


    print 'Running Test #2: Invalid arg'
    try:
        test_invalid_arg()
        print '    Failure: Test #2 Failed'
    except ValueError:
        print '    Success: Test #2 Passed'


    print 'Running Test #3: Line'
    try:
        print '    Manual check median line is visible'
        test_line()
        print '    Success: Test #3 Passed'
    except ValueError:
        print '    Failure: Test #3 Failed'


    print 'Running Test #4: Point'
    try:
        print '    Manual check that median points are shown'
        test_point()
        print '    Success: Test #4 Passed'
    except ValueError:
        print '    Failure: Test #4 Failed'

    print 'Running Test #5: None'
    try:
        print '    Manual check that no median is shown'
        test_no_median()
        print '    Success: Test #5 Passed'
    except ValueError:
        print '    Failure: Test #5 Failed'

