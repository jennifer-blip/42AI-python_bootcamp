from ImageProcessor import ImageProcessor

# xpoints = np.array([0, 6, 1, 8])
# ypoints = np.array([0, 6, 10, 16])

# plt.plot(xpoints, ypoints, marker='*')
# plt.plot(ypoints, marker='+')
# plt.plot(xpoints, marker='D')
# plt.show()
imp=ImageProcessor()
arr = imp.load("./images.jpg")
imp.display(arr)