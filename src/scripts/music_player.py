from PyQt5 import QtMultimedia
from PyQt5.QtCore import QUrl
from ui_constants import *


class MusicPlayer:
	def __init__(self):
		self.__player = QtMultimedia.QMediaPlayer()
		self.__player.setVolume(5)
		self.__music_list = [
			"auto",                 # 0     o_O
			"mem",                  # 1     O_o
			"pole-chudes-baraban",  # 2     o_O
			"pole_letter_correct",  # 3     O_o
			"pole_letter_wrong",    # 4     o_O
			"winner_music",         # 5     O_o
			"yakubovich_god"        # 6     o_O
		]

	def play_sound(self, sound_name: str):
		if sound_name in self.__music_list:
			self.__player.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile(MEDIA_DIR + sound_name + ".mp3")))
		self.__player.play()

	def stop(self):
		self.__player.stop()