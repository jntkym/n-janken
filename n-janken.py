#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import codecs
import argparse
import random

def main(args):
  candidates = args
  for i in range(0, len(candidates)):
    # TODO: implement "aiko"
    print candidates[i].decode('utf-8'), (random.choice(['✊', '✌️', '✋'])).decode('utf-8')

if __name__ == '__main__':
  sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

  # TODO: add arg for simple function
  parser = argparse.ArgumentParser()
  parser.add_argument("-name", help="list of name", nargs='+')
  args = parser.parse_args()

  main(args.name)
