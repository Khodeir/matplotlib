from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy.random import normal


# Creating tests for colors

# test when no widths arg is passed
def test_widths_default():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax = fig.add_subplot(111)
        ax.violinplot(data)
        show()

# test when the widths input is scaling down more than the default
def test_widths_smaller_than_default_scaler():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax = fig.add_subplot(111)
        ax.violinplot(data, widths=0.25)
        show()

# test when the widths input is scaling up more than the default
def test_widths_larger_than_default_scaler():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax = fig.add_subplot(111)
        ax.violinplot(data, widths=0.95)
        show()

# test when the widths input is not a scaler float and is an array
def test_widths_incorrect_input_as_list():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax = fig.add_subplot(111)
        ax.violinplot(data, widths=[0.2, 0.5])
        show()



if __name__=="__main__":

    print 'Running Test #1: Default width should be set if not specified'
    try:
        print '    Manual check that graphs are default width (0.75)'
        test_widths_default()
        print '    Success: Test #1 Passed (it build and displayed)'
    except ValueError:
        print '    Failure: Test #1 Failed to run'


    print 'Running Test #2: Widths smaller than default scaler'
    try:
        print '    Manual check that graphs width is smaller than the default'
        test_widths_smaller_than_default_scaler()
        print '    Success: Test #2 Passed (it build and displayed)'
    except ValueError:
        print '    Failure: Test #2 Failed to run'


    print 'Running Test #3: Widths larger than default scaler'
    try:
        print '    Manual check that graphs width is larger than the default'
        test_widths_larger_than_default_scaler()
        print '    Success: Test #3 Passed (it build and displayed)'
    except ValueError:
        print '    Failure: Test #3 Failed to run'


    print 'Running Test #4: Widths is not a scaler and is an array'
    try:
        test_widths_incorrect_input_as_list()
        print '    Manual check that graphs width is default'
        print '    Success: Test #4 Passed'
    except ValueError:
        print '    Failure: Test #4 Failed to run'


   