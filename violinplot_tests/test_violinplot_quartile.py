from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy.random import normal


# Creating tests for show/hide quartile box.

# test when quartile arg not given.
def test_no_arg():
        data = [normal(size=100) for i in range(3)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5)
        show()

# test when invalid (not true or false) quartile arg given
def test_invalid_arg():
        data = [normal(size=100) for i in range(3)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, quartile="apples")
        show()

# testing when quartile set to true.
def test_true_quartile():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, quartile=True)
        show()

# testing when quartile set to false.
def test_false_quartile():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, quartile=False)
        show()

# testing when quartile set to true with split true.
def test_split():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, quartile=True, split=True)
        show()

if __name__=="__main__":
# put tests here

    print 'Running Test #1: No arg'
    try:
        print '    Manual check that quartile are not shown'
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


    print 'Running Test #3: True quartile'
    try:
        print '    Manual check quartile are visible'
        test_true_quartile()
        print '    Success: Test #3 Passed'
    except ValueError:
        print '    Failure: Test #3 Failed'


    print 'Running Test #4: False quartile'
    try:
        print '    Manual check that quartile are not visible'
        test_false_quartile()
        print '    Success: Test #4 Passed'
    except ValueError:
        print '    Failure: Test #4 Failed'

    print 'Running Test #5: True quartile'
    try:
        print '    Manual check quartile are visible'
        test_split()
        print '    Success: Test #5 Passed'
    except ValueError:
        print '    Failure: Test #5 Passed'
