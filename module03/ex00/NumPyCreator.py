import numpy as np
from numpy.random import default_rng 

class NumPyCreator :

	def __init__(self):
		pass
	
	def from_list(self, lst, dtype=None):
		"""takes a list or nested lists and returns its corresponding Numpy array"""
		if not isinstance(lst, list):
			return None
		l = len(lst[0])
		for sublist in lst :
			if len(sublist) != l :
				return None 
		return np.array(lst, dtype=dtype)

	def from_tuple(self, tpl, dtype=None):
		"""takes a tuple or nested tuples and returns its corresponding Numpy array"""
		if not isinstance(tpl, tuple):
			return None
		return np.array(tpl, dtype=dtype)

	def from_iterable(self, itr, dtype=None):
		"""takes an iterable and returns an array which contains all of its elements"""
		return np.array(list(itr), dtype=dtype)

	def from_shape(self, shape, value=0, dtype=None):
		"""returns an array filled with the same value.
		The first argument is a tuple which specifies the shape of the array, and the second argument specifies the value of the elements. 
		This value must be 0 by default."""
		if not isinstance(shape, tuple) :
			return None
		return np.full(shape, value, dtype=None)
	
	def random(self, shape, dtype=None):
		"""returns an array filled with random values. It takes as an
		argument a tuple which specifies the shape of the array"""
		if not isinstance(shape, tuple) :
			return None
		return default_rng(42).random(shape, dtype=dtype)
	
	def identity(self, n, dtype=None):
		"""returns an array representing the identity matrix of size n"""
		if not isinstance(n, int) :
			return None
		return np.eye(n, dtype=dtype)