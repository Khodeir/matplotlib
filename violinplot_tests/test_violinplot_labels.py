from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy.random import normal


# Creating tests for tick labels.

# test when invalid labels arg passed
def test_invalid_labels():
        data = [normal(size=100) for i in range(3)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        labels="OH NOES"
        ax2.violinplot(data, widths=0.5, alpha=0.5, vert=False, plot_labels=labels)
        show()

# test when no label args passed
def test_no_labels():
        data = [normal(size=100) for i in range(3)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, alpha=0.5, vert=False)
        show()

# testing when empty label list is passed
def test_empty_labels():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        labels = []
        ax2.violinplot(data, widths=0.5, alpha=0.5, vert=False, plot_labels=labels)
        show()

# testing when labels are passed (#labels = #plots)
def test_equal_labels():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        labels = ["A", "B"]
        ax2.violinplot(data, widths=0.5, alpha=0.5, vert=False, plot_labels=labels)
        show()

# testing when labels are passed (#labels < #plots)
def test_less_labels():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        labels = ["A"]
        ax2.violinplot(data, widths=0.5, alpha=0.5, vert=False, plot_labels=labels)
        show()

# testing when labels are passed (#labels > #plots)
def test_more_labels():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        labels = ["A", "B", "C"]
        ax2.violinplot(data, widths=0.5, alpha=0.5, vert=False, plot_labels=labels)
        show()

# testing when labels are passed and vertical is set.
def test_label_vertical():
        data = [normal(size=100) for i in range(2)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        labels = ["A", "B"]
        ax2.violinplot(data, widths=0.5, alpha=0.5, plot_labels=labels)
        show()



if __name__=="__main__":
# put tests here

    print 'Running Test #1: Invalid labels'
    try:
        test_invalid_labels()
        print '    Failure: Test #1 Passed'
    except ValueError:
        print '    Success: Test #1 Failed'


    print 'Running Test #2: No labels'
    try:
        print '    Manual check that violins are numbered'
        test_no_labels()
        print '    Success: Test #2 Passed'
    except ValueError:
        print '    Failure: Test #2 Failed'


    print 'Running Test #3: Empty Labels'
    try:
        print '    Manual check violins are numbered'
        test_empty_labels()
        print '    Success: Test #3 Passed'
    except ValueError:
        print '    Failure: Test #3 Passed'


    print 'Running Test #4: # labels = # plots'
    try:
        print '    Manual check that graphs are all labeled'
        test_equal_labels()
        print '    Success: Test #4 Passed'
    except ValueError:
        print '    Failure: Test #4 Failed'


    print 'Running Test #5: # labels < # plots'
    try:
        print '    Manual check that graphs are all labeled except one'
        test_less_labels()
        print '    Success: Test #5 Passed'
    except ValueError:
        print '    Failure: Test #5 Failed'


    print 'Running Test #6: # labels > # plots'
    try:
        print '    Manual check that graphs are all labeled (no overflow)'
        test_more_labels()
        print '    Success: Test #6 Passed'
    except ValueError:
        print '    Failure: Test #6 Failed'


    print 'Running Test #7: labels on a vertical graph'
    try:
        print '    Manual check that graphs are all labeled'
        test_label_vertical()
        print '    Success: Test #7 Passed'
    except ValueError:
        print '    Failure: Test #7 Failed'