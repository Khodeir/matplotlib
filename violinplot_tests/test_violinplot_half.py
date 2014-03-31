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
<<<<<<< HEAD
        ax2.violinplot(data, widths=0.75, title='Not Split Vert', alpha=0.5, split=False)
=======
        ax2.violinplot(data, widths=0.5, title='Not Split Vert', alpha=0.5, vert=True, split=False)
>>>>>>> 241012b888bb2e5c4ad4b92d44931792b72e744e
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
        ax2.violinplot(data, widths=0.75, title='Not Split Vert', alpha=0.5)
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
        ax2.violinplot(data, widths=0.75, title='Even Split Vertical', alpha=0.5, split=True)
        show()

# testing vetical even number of plots
def test_vert_odd_plots():
        data = [normal(size=100) for i in range(7)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.75, title='Odd Split Vertical', alpha=0.5, split=True)
        show()

# testing vetical even number of plots with custom labels
def test_vert_odd_plots_labels():
        data = [normal(size=100) for i in range(7)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.75, title='Odd Split Vertical Custom labels', alpha=0.5,
                    split=True, plot_labels=['Plot 1', 'Plot 2', 'Plot 3', 'Plot 4', 'Plot 5',
                                                        'Plot 6', 'Plot 7'])
        show()

# testing vetical even number of plots with custom labels
def test_vert_even_plots_labels():
        data = [normal(size=100) for i in range(8)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.75, title='Even Split Vertical Custom labels', alpha=0.5,
                    split=True, plot_labels=['P1', 'P2', 'P3', 'P4', 'P5',
                                                        'P6', 'P7', 'P8'])
        show()

# testing horizontal even number of plots with custom labels
def test_horizontal_even_plots_labels():
        data = [normal(size=100) for i in range(8)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.75, title='Even Split Horizontal Custom labels', alpha=0.5, vert=False, split=True, plot_labels=['Pl 1', 'Pl 2', 'Pl 3', 'Pl 4', 'Pl 5',
                                                        'Pl 6', 'Pl 7', 'Pl 8'])
        show()

# testing horizontal odd number of plots with custom labels
def test_horizontal_odd_plots_labels():
        data = [normal(size=100) for i in range(7)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.75, title='Even Split Horizontal Custom labels', alpha=0.5,
                    vert=False, split=True, plot_labels=['Violin 1', 'Violin 2', 'Violin 3', 'Violin 4', 'Violin 5',
                                                        'Violin 6', 'Violin 7'])
        show()

# testing vertical large even number of plots
def test_vert_large_even_plots():
        data = [normal(size=100) for i in range(100)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.75, title='Even Split Vertical', alpha=0.5, split=True)
        show()

# testing vertical large odd number of plots
def test_vert_large_odd_plots():
        data = [normal(size=100) for i in range(101)]
        fig=figure()
        ax2 = fig.add_subplot(111)
        ax2.violinplot(data, widths=0.75, title='Even Split Vertical', alpha=0.5, split=True)
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
    except:
        print ("Failure: test_vert_even_plots() failed; unable to draw "
            "even number of split vertical violin plots.")

    try:
        test_vert_odd_plots()
    except:
        print ("Failure: test_vert_even_plots() failed; unable to draw "
            "odd number of split vertical violin plots.")

    try:
        test_vert_odd_plots_labels()
    except:
        print ("Failure: test_vert_odd_plots_labels() failed; unable to draw "
            "odd number of split vertical violin plots, with custom labels.")

    try:
        test_vert_even_plots_labels()
    except:
        print ("Failure: test_vert_even_plots_labels() failed; unable to draw "
            "even number of split vertical violin plots, with custom labels.")

    try:
        test_horizontal_even_plots_labels()
    except:
        print ("Failure: test_horizontal_even_plots_labels() failed; unable to"
             " draw even number of split horizontal violin plots, with custom "
             "labels.")

    try:
        test_horizontal_odd_plots_labels()
    except:
        print ("Failure: test_horizontal_odd_plots_labels() failed; unable to"
             " draw odd number of split horizontal violin plots, with custom "
             "labels.")

    try:
        test_vert_large_even_plots()
    except:
        print ("Failure: test_vert_large_even_plots() failed; unable to"
             " draw large even number of split horizontal plots.")

    try:
        test_vert_large_odd_plots()
    except:
        print ("Failure: test_vert_large_odd_plots() failed; unable to"
             " draw large odd number of split horizontal plots.")
