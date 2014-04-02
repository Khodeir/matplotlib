from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
from numpy.random import normal
import sys
import unittest

class TestScipyRequirement(unittest.TestCase):
	def test_scipy_requirement(self):
		# Set the default system module for scipy as None
		sys.modules['scipy'] = None
		data = [normal(size=100) for i in range(5)]
		fig = figure()
		ax = fig.add_subplot(111)
		# Violinplot function should raise an error due to lack of scipy module
		self.assertEquals(ax.violinplot(data), None)

if __name__=="__main__":
	# Run scipy unittest
	unittest.main()