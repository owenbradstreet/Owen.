# Developed by Owen Bradstreet.
import os, time, math

try:
	import replit
except ImportError:
	print("Not running on repl.it")
	onReplit = False
else:
	onReplit = True

def clear(onReplit=True):
	if (replit):
		replit.clear()
	else:
		os.system("clear")

def getDistance(pos1, pos2):
	return math.sqrt(((pos1[0] - pos2[0])**2) + ((pos1[1] - pos2[1])**2))

def metresToLy(distance):
	return distance*(1.057001*(10**16))

class Entity:
	def __init__(self, name, age):
		pass

class World:
	def __init__(self, name, age, faction, rep, mapMatrix):
		self._name = name
		self._age = age
		self._faction = faction
		self._rep = rep
		self._mapMatrix = mapMatrix
	def getName(self):
		return self._name
	def getAge(self):
		return self._age
	def getFaction(self):
		return self._faction
	def getRep(self):
		return self._rep
	def getMapMatrix(self):
		return self._mapMatrix

class Location:
	def __init__(self, name, age, faction, rep, mapMatrix, entities):
		self._name = name
		self._age = age
		self._rep = rep
		self._faction = faction
		self._mapMatrix = mapMatrix
		self._entities = entities
	def getName(self):
		return self._name
	def getAge(self):
		return self._age
	def getFaction(self):
		return self._faction
	def getRep(self):
		return self._rep
	def getMapMatrix(self):
		return self._mapMatrix
	def getEntities(self):
		return self._entities
	def getEntityClosestTo(self, pos):
		closestEntity = [0,9223372036854775807]
		for entity in self._entities:
			if (getDistance(pos, entity.pos) < closestEntity[1]):
				closestEntity = [entity, getDistance(pos, entity.pos)]
		if (closestEntity[0] == 0):
			return None
		else:
			return closestEntity[0]

while True:
	clear(replit)
	print("     _/_/                                             \n  _/    _/  _/      _/      _/    _/_/    _/_/_/      \n _/    _/  _/      _/      _/  _/_/_/_/  _/    _/     \n_/    _/    _/  _/  _/  _/    _/        _/    _/      \n _/_/        _/      _/        _/_/_/  _/    _/  _/\n\n")
	print("- Start a new game (new)")
	print("- Load an existing game (load)")
	print("- Options (options)")
	print("- Exit (exit)\n")
	i = input("> ")
	if (i in ["new", "new game", "start a new game", "n"]):
		pass
	elif (i in ["load", "load an existing game", "load existing", "l"]):
		pass
	elif (i in ["options", "option", "o"]):
		pass
	elif (i in ["exit", "quit", "e", "q"]):
		print("Goodbye, user.")
	else:
		print("Invalid command.")
		time.sleep(1)