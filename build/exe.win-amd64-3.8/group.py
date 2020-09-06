
# so many useless function
# just so many useless functions

class Group:
	def __init__(self, name=""):
		self.__objects = []
		self.name = name
		return

	def __iter__(self):
		return iter(self.__objects)

	def __repr__(self):
		module = self.__class__.__module__
		class_name = self.__class__.__name__
		memory_location = hex(id(self))
		return f"<{module}.{class_name} object at {memory_location}>"

	def __str__(self):
		out = f"Group {repr(self)} contains:\n"
		for obj in self:
			out += str(obj)
		if self.is_empty():
			out += "None\n"
		return out

	def __len__(self):
		return len(self.__objects)

	def __eq__(self, other):
		return len(self) == other

	def __lt__(self, other):
		return len(self) < other

	def __ne__(self, other):
		return not self == other

	def __getitem__(self, index):
		return self.__objects.__getitem__(index)

	# this is my favorite function
	# please don't tell __repr__
	@classmethod
	def create(cls, arr):
		group = Group()
		group.append(arr)
		return group

	def blit(self):
		for obj in self:
			obj.blit()
		return

	def append(self, other):
		if type(other) == list:
			for item in other:
				self.append(item)
		else:
			self.__objects.append(other)
		return

	def is_empty(self):
		return len(self) == 0

	def remove(self, func, count=False):
		coun = 0
		for obj in self:
			if func(obj):
				coun += 1
				self.__objects.remove(obj)
		if count:
			return coun
		return
	pass