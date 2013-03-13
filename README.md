LanguageTrials
==============

Putting languages through a gauntlet and rating them based on their performance


The Trial
=========

The trial is to compute the standard deviation of a large chunk of randomly generated data, transmitted over a local port.

The trial has 3 parts: client, server and controller.

Each language must set up a webserver.  When the server is set up, it will load each of the 100 random documents into memory.  Upon receiving a request to the root directory on port 8080, the server will respond with one of those files.  The server will not repeat a file.  After the server has served each file, it will shut down.

Each language must also set up a client.  The client must consume one document from the server.  The client will then do whatever computation is nessary and report its results to the controller.

Each language must also set up a controller.  The controller setup up the server, then spawns 100 client processes and aggreggates their results.  The controller must then print the correct integer truncated standard deviation to standard out and close with no error code.


The Rules
=========

All code must be written in the specified language.

No external libraries are to be used.

Lines may not be broken unless they represent different logical statements, even if allowed by language syntax.

Each randomly generated file will have 5000 random numbers, each on a seperate line, and nothing else.


Judgement
=========

Each language will be judged on the following criteria:

1.  strlen: how many total characters are involved in the code (including documentation)
2.  longest line: how many characters on the longest line of code
3.  time: how long from when the controller was first invoked to its completion
4.  writability: how long did the code take to write
5.  readability: subjective score 1-100, how easy is the code to read
