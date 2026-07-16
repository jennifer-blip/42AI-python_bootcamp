class Vector :
	def __init__(self, values):
		if isinstance(values, list) :
			if not self.check_format(values) :
				raise ValueError (f"{values} requires a list of list of FLOATS [[x],[y],..] or [[x, y, z,...]], a tuple of 2 integer or 1 integer")
			for x in values :
				if isinstance(x, list) :
					self.values = values
				else :
					raise ValueError (f"{values} requires a list of list of FLOATS [[x],[y],..] or [[x, y, z,...]], a tuple of 2 integer or 1 integer")
		if isinstance(values, tuple) :
			if len(values) > 2 :
				raise ValueError (f"{values} requires a list of list of FLOATS [[],[],..] or [[x, y, z,...]], a tuple of 2 integer or 1 integer")
			self.values = [[float(elm)] for elm in range(values[0], values[1])]
		if isinstance(values, int) :
			self.values = [[float(x)] for x in range(values)]
		if len(self.values) > 1 :
			self.shape = (len(self.values), 1)
			self.size = len(self.values)
		else :
			for x in self.values :
				self.shape = (1, len(x))
				self.size = len(x)

	def check_format(self, values) :
		for x in values :
			if isinstance(x, list) :
				for y in x :
					if not isinstance(y, float) :
						return False
			else :
				if not isinstance(x, float):
					return False
		return True

	def flatten(self) :
		result = []
		for sublist in self.values :
			for value in sublist :
				result.append(value)
		return result

	def T(self) :
		if self.shape[0] == 1 :#transpose from row vector to column vector
			result = [[]]
			for value in self.values[0] :
				result.append([value])
			result.pop(0)
			# result = [[value] for sublist in self.values for value in sublist]
			print(result)
			return Vector(result)
		else :#transpose from column vector to row vector
			result = []
			for sublist in self.values :
				# for value in sublist[0] :
					result.append(sublist)
			print (result)
			return Vector(result)

	def dot(self, vec) :
		if not isinstance(vec, Vector) :
			raise ValueError (f"cannot caluculate dot product : {vec} is not an instance of the Vector class")
		if self.size != vec.size :
			raise ValueError (f"cannot calculate dot product : {self.values} and {vec.values} are not of the same dimension")
		else :
			i = 0
			result = 0
			print(f"dot product of {self.values} and {vec.values} = :", end= " ")
			vec1 = self.flatten()
			vec2 = vec.flatten()
			for i in range(self.size) :
				result += vec1[i % self.size] * vec2[(i + 1) % self.size]
			print(result)
			return result
	
	def __add__(self, vec) :
		if not isinstance(vec, Vector) :
			raise ValueError (f"Unable to add : {vec} is not an instance of the Vector class")
		if self.size != vec.size :
			raise ValueError ("Unable to add : vectors don't have the same dimension ")
			return
		vec1 = self.flatten()
		vec2 = vec.flatten()
		vec3 = []
		for i in range(self.size) :
			vec3.append([vec1[i] + vec2[i]])
		result = Vector(vec3)
		return result
	def __radd__(self, vec) :
		return self.__add__(vec)
	def __sub__(self, vec) :
		if not isinstance(vec, Vector) :
			raise ValueError (f"Unable to subtract : {vec} is not an instance of the Vector class")
		if self.size != vec.size :
			raise ValueError ("Unable to subtract : vectors don't have the same dimension ")
			return
		vec1 = self.flatten()
		vec2 = vec.flatten()
		vec3 = []
		for i in range(self.size) :
			vec3.append([vec1[i] - vec2[i]])
		result = Vector(vec3)
		return result
	def __rsub__(self, vec) :
		return vec.__sub__(self)
	def __truediv__(self, sca) :
		if not isinstance(sca, (int, float)) :
			raise ValueError (f"Unable to divide : {sca} is not a scalar")
		if sca == 0 :
			raise ValueError (f"Unable to divide by zero scalar")
		vec1 = self.flatten()
		vec2 = []
		for i in range(self.size) :
			vec2.append([vec1[i] / sca])
		result = Vector(vec2)
		return result
	def __rtruediv__(self, sca) :
		raise NotImplementedError ("Division of a scalar by a Vector is not defined here.")
	def __mul__(self, sca) :
		if not isinstance(sca, (int, float)) :
			raise ValueError (f"Unable to multiply : {sca} is not a scalar")
		vec1 = self.flatten()
		vec2 = []
		for i in range(self.size) :
			vec2.append([vec1[i] * sca])
		result = Vector(vec2)
		return result
	def __rmul__(self, sca) :
		return self.__mul__(sca)
	def __str__(self) :
		if self.shape[0] == 1 :
			return "[" + ", ".join(str(round(v, 2)) for v in self.values[0]) + "]"
		else:
			return "[" + ", ".join(f"[{round(row[0], 1)}]" for row in self.values) + "]"
	def __repr__(self) :
		return f"({self.values})"
	# # # must be identical, i.e we expect that print(vector) and vector within python interpretor to behave