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
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color="m")
        show()

# testing when invalid facecolor used
def test_invalid_facecolor():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color="waffles")
        show()

# testing when valid 'y' edgecolor used
def test_valid_edgecolor():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color="y")
        show()

# testing when invalid edgecolor used
def test_invalid_edgecolor():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color="waffles")
        show()

# testing when passing multiple colors in when colors match number of violins
def test_valid_multiple_colors_same_as_range():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color="rgbcm")
        show()

# testing when passing multiple colors in when colors don't match number of violins
def test_valid_multiple_colors_diff_to_range():
        data = [normal(size=100) for i in range(10)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Colors', alpha=0.5, vert=False, color="rgbcm")
        show()





if __name__=="__main__":
# put tests here

    try:
        test_no_color()
    except ValueError:
        print 'Failure: Invalid Color Test Failed'

    try:
        test_valid_r_color()
    except ValueError:
        print 'Failure: Invalid Color Test Failed'

    try:
        test_valid_num_color()
    except ValueError:
        print 'Failure: Invalid Color Test Failed'

    try:
        test_valid_hexa_color()
    except ValueError:
        print 'Failure: Invalid Color Test Failed'

    try:
        test_invalid_color()
    except ValueError:
        print 'Success: Invalid Color Test Failed'

    try:
        test_valid_facecolor()
    except ValueError:
        print 'Failure: Invalid Edgecolor Test Failed'

    try:
        test_invalid_facecolor()
    except ValueError:
        print 'Success: Invalid Facecolor Test Failed'

    try:
        test_valid_edgecolor()
    except ValueError:
        print 'Failure: Invalid Edgecolor Test Failed'

    try:
        test_invalid_edgecolor()
    except ValueError:
        print 'Success: Invalid Edgecolor Test Failed'

    try:
        test_valid_multiple_colors_same_as_range()
    except ValueError:
        print 'Failure: Invalid Edgecolor Test Failed'

    try:
        test_valid_multiple_colors_diff_to_range()
    except ValueError:
        print 'Failure: Invalid Edgecolor Test Failed'
