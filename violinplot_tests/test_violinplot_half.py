from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy.random import normal
import traceback


# Creating tests for colors

# test when we want to draw regular normal violins
def test_no_split():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Not Split', alpha=0.5, vert=False, split=False)
        show()

# testing when we want to draw regular vertical violins
def test_no_split_vert():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Not Split Vert', alpha=0.5, vert=True, split=False)
        show()

# test when we want to draw regular normal violins without passing the 'split' arg
def test_no_split_noarg():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Not Split', alpha=0.5, vert=False)
        show()

# testing when we want to draw regular vertical violins without passing 'split' arg
def test_no_split_vert_noarg():
        data = [normal(size=100) for i in range(5)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Not Split Vert', alpha=0.5, vert=True)
        show()

# testing horizontal even number of plots
def test_horizontal_even_plots():
        data = [normal(size=100) for i in range(6)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Even Split', alpha=0.5, vert=False, split=True)
        show()

# testing horizontal odd number of plots
def test_horizontal_odd_plots():
        data = [normal(size=100) for i in range(7)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Odd Split', alpha=0.5, vert=False, split=True)
        show()

# testing vertical even number of plots
def test_vert_even_plots():
        data = [normal(size=100) for i in range(6)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Even Split', alpha=0.5, vert=True, split=True)
        show()

# testing vetical even number of plots
def test_vert_odd_plots():
        data = [normal(size=100) for i in range(7)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.5, title='Even Split', alpha=0.5, vert=True, split=True)
        show()


if __name__=="__main__":
# put tests here

    try:
        test_no_split()
    except:
        print ("Failure: test_no_split() failed; unable to draw regular "
            "horizontal violin plots.")

    try:
        test_no_split_vert()
    except:
        print ("Failure: test_no_split_vert() failed; unable to draw regular "
            "vertical violin plots.")

    try:
        test_no_split_noarg()
    except:
        print ("Failure: test_no_split_noarg() failed; unable to draw regular "
            "horizonal violin plots, without specifying the 'split' arg")

    try:
        test_no_split_vert_noarg()
    except:
        print ("Failure: test_no_split_vert_noarg() failed; unable to draw "
            "vertical violin plots, without specifying the 'split' arg.")

    try:
        test_horizontal_even_plots()
    except:
        print ("Failure: test_horizontal_even_plots() failed; unable to draw "
            "even number of split horizontal violin plots.")

    try:
        test_horizontal_odd_plots()
    except:
        print traceback.format_exc()
        print ("Failure: test_horizontal_odd_plots() failed; unable to draw "
            "odd number of split horizontal violin plots.")

    try:
        test_vert_even_plots()
    except Exception as e:
        print str(e)
        print ("Failure: test_vert_even_plots() failed; unable to draw "
            "even number of split vertical violin plots.")

    try:
        test_vert_odd_plots()
    except Exception as e:
        print str(e)
        print ("Failure: test_vert_even_plots() failed; unable to draw "
            "odd number of split vertical violin plots.")
