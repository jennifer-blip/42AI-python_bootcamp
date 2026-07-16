from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

class ImageProcessor :
	def load(self, path): 
		"""opens the PNG file specified by the path argument and returns an
		array with the RGB values of the pixels in the image. It must display a message
		specifying the dimensions of the image (e.g. 340 x 500)."""
		try :
			img = np.asarray(Image.open(path))
			print(f"Loading image of {img.shape[0]} x {img.shape[1]} dimension")
			return img
		except (FileNotFoundError, OSError) as e:
			print (e)
			return None

	def display(self, array): 
		"""takes a numpy array as an argument and displays the corresponding RGB image."""
		if not isinstance(array, np.ndarray) :
			print("None")
		else:
			print(repr(array))