#!/usr/bin/env python

import math

from multiprocessing import Process, Pipe

import Client
import Server

def merge_populations(pops):
  while len(pops) > 1:
    a = pops.pop()
    b = pops[0]
    new_size = a[2] + b[2]
    weighted_variances = ((a[0] * a[0] * a[2]) + (b[0] * b[0] * b[2])) / new_size
    mean_variance = math.pow(a[1] - b[1], 2.0) * (a[2] * b[2]) / math.pow(new_size, 2.0)
    new_std = math.sqrt(weighted_variances + mean_variance)
    new_mean = (a[1] * a[2] + b[1] * b[2]) / (new_size)
    pops[0] = (new_std, new_mean, new_size)


if __name__ == '__main__':
  srv_listen, srv_speak = Pipe()
  server = Process(target=Server.run, args=(srv_speak,))
  server.start()
  srv_listen.recv()
  client_pipes = [Pipe() for x in xrange(100)]
  client_procs = [Process(target=Client.run, args=(x[1],)) for x in client_pipes]
  for proc in client_procs:
    proc.start()
  results = (x[0].recv() for x in client_pipes)
  pops = [(float(x[0]), float(x[1]), 5000) for x in results]
  for proc in client_procs:
    proc.join()
  server.join()
  merge_populations(pops)
  print int(pops[0][0])
