from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy.random import normal


# Creating tests for colors

# test when no covariance_factor arg is passed, should be scotts factor
def test_covariance_default():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax = fig.add_subplot(111)
        ax.violinplot(data)
        show()

# test covariance_factor is set to custom factor for steepness
def test_covariance_custom_steep():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax = fig.add_subplot(111)
        cv = lambda : 0.1
        ax.violinplot(data, covariance_factor=cv)
        show()

# test covariance_factor is set to custom factor for flatness
def test_covariance_custom_flat():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax = fig.add_subplot(111)
        cv = lambda : 0.95
        ax.violinplot(data, covariance_factor=cv)
        show()



if __name__=="__main__":

    print 'Running Test #1: Default covariance_factor should be set if not specified'
    try:
        print '    Manual check that graphs are using scotts factor'
        test_covariance_default()
        print '    Success: Test #1 Passed (it build and displayed)'
    except ValueError:
        print '    Failure: Test #1 Failed to run'


    print 'Running Test #3: covariance_factor is custom set for steep curves'
    try:
        print '    Manual check that graph has very wavy/steep curves compared to default'
        test_covariance_custom_steep()
        print '    Success: Test #3 Passed (it build and displayed)'
    except ValueError:
        print '    Failure: Test #3 Failed to run'


    print 'Running Test #4: covariance_factor is custom set for flat curves'
    try:
        print '    Manual check that graph is very flat compared to default'
        test_covariance_custom_flat()
        print '    Success: Test #4 Passed (it build and displayed)'
    except ValueError:
        print '    Failure: Test #4 Failed to run'
