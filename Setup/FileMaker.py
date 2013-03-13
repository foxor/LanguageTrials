#!/usr/bin/env python

import random
import os

if __name__ == '__main__':
  path,_ = os.path.split(os.path.realpath(__file__))
  for i in xrange(1,101):
    fptr = open("%s/Files/%d" % (path, i), 'w')
    for n in xrange(5000):
      fptr.write("%d\n" % random.randint(1, 100001))
    fptr.close()
