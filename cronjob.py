#!/usr/bin/env python
from __future__ import print_function
import subprocess
import os
import random

PLAY_COUNT = 3
#MEDIA_PATH = '/home/williamchi/mp3/'
MEDIA_PATH = '/home/pi/PeppaPig_MP3/'

"""
>>> import subprocess
>>> subprocess.Popen(['mpg123', '-q', 'Peppa.Pig.S4E01.Potato.City.MP3']).wait()
0   

"""


def get_play_list(count):

    media_list = [i for i in os.listdir(MEDIA_PATH) if i.endswith('MP3') or i.endswith('mp3')]
    play_list = ["%s%s" % (MEDIA_PATH, i) for i in random.sample(media_list, int(count))]

    return play_list


def play_media(media_file_path):

    subprocess.Popen(['mpg123', '-q', media_file_path]).wait()


if __name__ == '__main__':

    for media in get_play_list(PLAY_COUNT):
        play_media(media)
