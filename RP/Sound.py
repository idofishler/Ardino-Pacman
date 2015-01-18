#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Sound(object):
	"""A sound"""

	def __init__(self, arg):
		super(Sound, self).__init__()
		self.arg = arg
		self.proc = subprocess.Popen("echo")

	def play(self):
		self.proc = subprocess.Popen(["/usr/bin/aplay", "/home/pi/VC/CSH6XuazmB8.wav"])

	def kill(self):
		subprocess.Popen.kill(self.proc)

	def isAlive(self):
		return self.proc.poll()
