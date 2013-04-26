#!/usr/bin/env python

import os
import re
import sys

_charCount = 0
def countChars(line):
  global _charCount
  _charCount += len(line)

_longestLine = 0
def measureLength(line):
  global _longestLine
  _longestLine = max(_longestLine, len(line))

_filter = re.compile(r"Result|\.class|\.pyc")

_functions = [countChars, measureLength]
def processLines(project):
  for fname in [x for x in os.listdir(project) if not _filter.search(x)]:
    fptr = open("%s/%s" % (project, fname), 'r')
    for line in fptr:
      for fn in _functions:
        fn(line)

#Printing one stat on each line:
# strlen
# longest line
# readability
# reusability
# writability
# dirtiness
def dumpOutput():
  print _charCount
  print _longestLine

if __name__ == '__main__':
  project = sys.argv[1]
  processLines(project)
  dumpOutput()
