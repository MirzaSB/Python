class Room(object):
	
	def __init__(self,name,description):
		self.name = name
		self.description = description
		self.paths = {}
	
	def go(self,direction):
		return self.paths.get(direction,None)
	
	def add_paths(self,paths):
		self.paths.update(paths)

	def remove_path(self,key_to_remove):
		self.paths.pop(key_to_remove, None)

	def room_size(self):
		return len(self.paths)

