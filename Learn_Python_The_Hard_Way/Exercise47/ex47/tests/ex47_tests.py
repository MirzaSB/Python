from nose.tools import *
from ex47.game import Room

def test_room():
	gold = Room("GoldRoom",
		""" This room has gold in it you can grab. There's a door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})

def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")

	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)

def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")

	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	assert_equal(start.go('west'),west)
	assert_equal(start.go('west').go('east'),start)
	assert_equal(start.go('down').go('up'),start)

def test_removal():
	room1 = Room("Room1", "Test Room1.")
	room2 = Room("Room2", "Test Room2.")
	room3 = Room("Room3", "Test Room3.")
	room1.add_paths({'Room2': room2})
	room1.add_paths({'Room3': room3})
	assert_equal(room1.room_size(),2)
	room1.remove_path("Room2")
	assert_equal(room1.room_size(),1)
	room1.remove_path("Room3")
	assert_equal(room1.room_size(),0)

