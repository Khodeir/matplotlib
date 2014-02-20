"""
Demo of the errorbar function.
"""
import matplotlib
matplotlib.use('QT4Agg')
matplotlib.rcParams['backend.qt4']='PySide'

import numpy as np
import matplotlib.pyplot as plt

with plt.xkcd():
	# example data
	x = np.arange(0.1, 4, 0.5)
	y = np.exp(-x)

	plt.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()

