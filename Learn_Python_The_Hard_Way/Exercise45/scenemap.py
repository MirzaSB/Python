import scene
import death
import waynetechboardroom
import batcave
import gotham_city_bridge
import maze
import finished

class Map(object):

	scenes = {
		'death': death.Death(),
		'waynetechboardroom': waynetechboardroom.WayneTechBoardRoom(),
		'batcave': batcave.BatCave(),
		'gotham_city_bridge': gotham_city_bridge.GothamCityBridge(),
		'maze': maze.Maze(),
		'finished': finished.Finished()
	}
	
	def __init__(self,start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)

