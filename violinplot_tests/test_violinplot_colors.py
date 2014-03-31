from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy.random import normal


# Creating tests for colors

# test when no color args passed
def test_no_color():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False)
        show()

# testing when valid 'r' color used
def test_valid_r_color():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color='r')
        show()

# testing when valid decimal color used
def test_valid_num_color():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color='0.75')
        show()

# testing when valid hexadecimal color used
def test_valid_hexa_color():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color="#0ef0ef")
        show()

# testing when invalid color used
def test_invalid_color():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color="waffles")
        show()

# testing when valid 'm' facecolor used
def test_valid_facecolor():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, facecolor="m")
        show()

# testing when invalid facecolor used
def test_invalid_facecolor():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, facecolor="waffles")
        show()

# testing when valid 'y' edgecolor used
def test_valid_edgecolor():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, edgecolor="y")
        show()

# testing when invalid edgecolor used
def test_invalid_edgecolor():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, edgecolor="waffles")
        show()

# testing when passing multiple colors in when colors match number of violins
def test_valid_multiple_colors_same_as_range():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color="rgbcm")
        show()

# testing when passing multiple colors in when colors don't match number of violins
def test_valid_multiple_colors_less_than_range():
        data = [normal(size=100) for i in range(10)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color="rgbcm")
        show()

# testing when passing multiple colors in when colors don't match number of violins
def test_valid_multiple_colors_greater_than_range():
        data = [normal(size=100) for i in range(3)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color="rgbcm")
        show()

def test_half_no_color():
        data = [normal(size=100) for i in range(9)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, split=True)
        show()

def test_half_one_color():
        data = [normal(size=100) for i in range(9)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, split=True, color='r')
        show()

def test_half_many_colors():
        data = [normal(size=100) for i in range(9)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, split=True, color='bgrcmyk')
        show()



if __name__=="__main__":
# put tests here

    print 'Running Test #1: No color values passed in'
    try:
        print '    Manual check that graphs are default color (blue)'
        test_no_color()
        print '    Success: Test #1 Passed'
    except ValueError:
        print '    Failure: Test #1 Failed'


    print 'Running Test #2: Valid color: r'
    try:
        print '    Manual check that graphs are all red'
        test_valid_r_color()
        print '    Success: Test #2 Passed'
    except ValueError:
        print '    Failure: Test #2 Failed'


    print 'Running Test #3: Valid color: 0.75'
    try:
        print '    Manual check that graphs are all grey'
        test_valid_num_color()
        print '    Success: Test #3 Passed'
    except ValueError:
        print '    Failure: Test #3 Passed'


    print 'Running Test #4: Valid color: #0ef0ef'
    try:
        print '    Manual check that graphs are all bright blue'
        test_valid_hexa_color()
        print '    Success: Test #4 Passed'
    except ValueError:
        print '    Failure: Test #4 Failed'


    print 'Running Test #5: Valid color: 0.75'
    try:
        test_invalid_color()
        print '    Failure: Test #5 Passed when it should have failed'
    except ValueError:
        print '    Success: Test #5 failed'


    print 'Running Test #6: Valid facecolor passed in'
    try:
        print '    Manual check that graphs faces are magenta'
        test_valid_facecolor()
        print '    Success: Test #6 Passed'
    except ValueError:
        print '    Failure: Test #6 failed'


    print 'Running Test #7: Invalid facecolor passed in'
    try:
        test_invalid_facecolor()
        print '    Failure: Test #7 Passed when it should have failed'
    except ValueError:
        print '    Success: Test #7 failed'


    print 'Running Test #8: Multiple colors where number of colors is same as number of violins'
    try:
        print '    Manual check that graphs are rgbcm from bottom to top'
        test_valid_multiple_colors_same_as_range()
        print '    Success: Test #8 Passed'
    except ValueError:
        print '    Failure: Test #8 failed'


    print 'Running Test #9: Multiple colors where we have more violins than colors'
    try:
        print '    Manual check that graphs are rgbcm from bottom to top in a loop'
        test_valid_multiple_colors_less_than_range()
        print '    Success: Test #9 Passed'
    except ValueError:
        print '    Failure: Test #9 failed'

    print 'Running Test #10: Multiple colors where we have fewer violins than colors'
    try:
        print '    Manual check that graphs are rgb from bottom to top in a loop'
        test_valid_multiple_colors_greater_than_range()
        print '    Success: Test #10 Passed'
    except ValueError:
        print '    Failure: Test #10 failed'

    print 'Running Test #11: Split violins, no color'
    try:
        print '    Manual check that graphs are alternating blue and green'
        test_half_no_color()
        print '    Success: Test #11 Passed'
    except ValueError, e:
        print '    Failure: Test #11 failed'
        print e

    print 'Running Test #12: Split violins, one color'
    try:
        print '    Manual check that graphs are all red'
        test_half_one_color()
        print '    Success: Test #12 Passed'
    except ValueError:
        print '    Failure: Test #12 failed'

    print 'Running Test #13: Split violins, many colors'
    try:
        print '    Manual check that graphs are alternating bgrcmyk'
        test_half_many_colors()
        print '    Success: Test #13 Passed'
    except ValueError:
        print '    Failure: Test #13 failed'
