#!/usr/bin/env python

from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import os

def server_state():
  global _findex
  _findex = 1
  def complete():
    return _findex > 100
  def file_coroutine():
    global _findex
    path,_ = os.path.split(os.path.realpath(__file__))
    while not complete():
      fptr = open("%s/../Setup/Files/%d" % (path, _findex), 'r')
      contents = fptr.read()
      fptr.close()
      _findex += 1
      yield contents
  return file_coroutine(), complete

files, complete = server_state()

class Handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "text/plain")
    self.end_headers()
    self.wfile.write(files.next())

  def log_message(self, format, *args):
    return

def run(pipe):
  httpd = HTTPServer(("localhost", 8080), Handler)
  pipe.send('online')
  while not complete():
    httpd.handle_request()
  pipe.close()
