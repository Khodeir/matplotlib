from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy.random import normal


# Creating tests for show/hide whiskers.

# test when whisker arg not given.
def test_no_arg():
        data = [normal(size=100) for i in range(3)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5)
        show()

# test when invalid (not true or false) whisker arg given
def test_invalid_arg():
        data = [normal(size=100) for i in range(3)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, whiskers="apples")
        show()

# testing when whiskers set to true.
def test_true_whiskers():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, whiskers=True)
        show()

# testing when whiskers set to false.
def test_false_whiskers():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, whiskers=False)
        show()

# testing when whiskers set to true with split true.
def test_split():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, whiskers=True, split=True)
        show()

if __name__=="__main__":
# put tests here

    print 'Running Test #1: No arg'
    try:
        print '    Manual check that whiskers are not shown'
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


    print 'Running Test #3: True whiskers'
    try:
        print '    Manual check whiskers are visible'
        test_true_whiskers()
        print '    Success: Test #3 Passed'
    except ValueError:
        print '    Failure: Test #3 Failed'


    print 'Running Test #4: False whiskers'
    try:
        print '    Manual check that whiskers are not visible'
        test_false_whiskers()
        print '    Success: Test #4 Passed'
    except ValueError:
        print '    Failure: Test #4 Failed'

    print 'Running Test #5: True whiskers'
    try:
        print '    Manual check whiskers are visible'
        test_split()
        print '    Success: Test #5 Passed'
    except ValueError:
        print '    Failure: Test #5 Passed'
