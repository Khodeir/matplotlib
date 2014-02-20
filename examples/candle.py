import matplotlib
matplotlib.use('QT4Agg')
matplotlib.rcParams['backend.qt4']='PySide'

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.finance



#with plt.xkcd():
quotes = [(1, 5, 6, 7, 4), (2, 6, 9, 9, 6), (3, 9, 8, 10, 8), (4, 8, 8, 9, 8), (5, 8, 11, 13, 7)]
ax = plt.gca()
h = matplotlib.finance.candlestick_ochl(ax, quotes, colorup='g', colordown='r')
plt.show()