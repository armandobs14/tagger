from argparse import ArgumentParser
from ShazamAPI import Shazam
from os import walk
import json
import sys
import os


class Tagger():

  def main(self):
    parser = ArgumentParser(description='Rename songs')

    # path
    parser.add_argument('--p', '--path',
                        help='Path to mp3 files', type=str)
    args = parser.parse_args()  # GET PARAMS

    _, _, files = next(walk(args.p))
    files = [f for f in files if f.endswith(".mp3")]
    for file_name in files:
      try:
        self.find_name(args.p, file_name)
      except Exception as e:
        print(e)

  def find_name(self, file_path, file_name):
    with open(file_path + file_name, 'rb') as song:
      song_conent = song.read()
      shazam = Shazam(song_conent)
      recognize_generator = shazam.recognizeSong()
      
      _, response = next(recognize_generator)
      song_title = response['track']['title']
      song_subtitle = response['track']['subtitle']
      new_name = f"{song_title} - {song_subtitle}.mp3"
      os.rename(file_path + file_name, file_path + new_name)
      return file_path + new_name
