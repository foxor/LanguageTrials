#!/usr/bin/env python

import urllib2
import math

def run(pipe):
  fptr = urllib2.urlopen('http://localhost:8080/')
  ints = [int(x) for x in fptr]
  mean = (1.0 * sum(ints)) / len(ints)
  std = math.sqrt(sum(math.pow(x - mean, 2.0) for x in ints))
  pipe.send([std, mean])
  pipe.close()
