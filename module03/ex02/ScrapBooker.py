import numpy as np

class ScrapBooker :
	def crop(self, array, dim, position=(0,0)):
		"""Crops the image as a rectangle via dim arguments (being the new height
		and width of the image) from the coordinates given by position arguments."""
		if not isinstance(array, np.ndarray) or not isinstance(dim, tuple) or not isinstance(position, tuple):
			return None
		if dim[0] > np.shape(array)[0] or dim[1] > np.shape(array)[1] or position[0]+dim[0] > np.shape(array)[0] or position[1]+dim[1] > np.shape(array)[1] :
			return None
		# delete les row superflus
		result = np.delete(array, np.s_[:position[0]] , 0)
		result = np.delete(result, np.s_[position[0]+dim[0]-1:], 0)
		# delete les column superflus
		result = np.delete(result, np.s_[:position[1]] , 1)
		result = np.delete(result, np.s_[position[1]+dim[1]:], 1)
		return result
		# return array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]

	def thin(self, array, n, axis):
		"""
		Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
		"""
		if not isinstance(array, np.ndarray) or not isinstance(n, int) or not isinstance(axis, int):
			return None
		if axis not in [0, 1] or n < 1 :
			return None
		if n > array.shape[axis] or n <= 1:
			return None
		return np.delete(array, np.s_[::n], axis)

	def juxtapose(self, array, n, axis):
		"""
		Juxtaposes n copies of the image along the specified axis.
		"""
		if not isinstance(array, np.ndarray) or not isinstance(n, int) or not isinstance(axis, int):
			return None
		if axis not in [0, 1] or n < 1 or n > 2147483647 or n <= 0 :
			return None
		return np.concatenate([array] * n, axis=axis)
		# return np.repeat(array, n, axis=axis)
	# def mosaic(self, array, dim):
	# 	"""
	# 	Makes a grid with multiple copies of the array. The dim argument specifies
	# 	the number of repetition along each dimensions.
	# 	Args:
	# 	-----
	# 	array:
	# 	dim:numpy.ndarray.
	# 	tuple of 2 integers.
	# 	Return:
	# 	-------
	# 	new_arr:
	# 	Nonemosaic numpy.ndarray.
	# 	(combinaison of parameters not compatible).
	# 	Raises:
	# 	-------
	# 	This function should not raise any Exception.
	# 	"""
	# 	if not isinstance(array, np.ndarray) or not isinstance(dim, tuple) :
	# 		return None