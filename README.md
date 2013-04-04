LanguageTrials
==============

Putting languages through a gauntlet and rating them based on their performance


The Trial
=========

The trial is to compute the standard deviation of a large chunk of randomly generated data, transmitted over a local port.

The trial has 3 parts: client, server and controller.

Each language must set up a webserver.  Upon receiving a request to the root directory on port 8080, the server will load one of those files and respond.  The server will not repeat a file.  After the server has served each file, it will shut down.

Each language must also set up a client.  The client must consume one document from the server.  The client will then do whatever computation is nessary and report its results to the controller.

Each language must also set up a controller.  The controller setup up the server, then spawns 100 client processes and aggreggates their results.  The controller must then print the correct integer truncated standard deviation to standard out and close with no error code.


The Rules
=========

All code must be written in the specified language.

No external libraries are to be used.

Lines may not be broken unless they represent different logical statements, even if allowed by language syntax.

Each randomly generated file will have 5000 random numbers between 1 and 100000, each on a seperate line, and nothing else.

Each client process will calculate the statistics of only one file, using the simple two step approach, and the controller will combine the populations.


Judgement
=========

Each language will be judged on the following criteria:

1.  strlen: how many total characters are involved in the code (including documentation).  Project with the fewest scores 100, project with the most scores 0, all others are lerp
2.  longest line: how many characters on the longest line of code.  Project with the shortest scores 100, project with the longest scores 0, all others are lerp
3.  readability: subjective score 1-100, how easy is the code to read
4.  reusability: % of characters in the codebase that change if this code is changed to give the maximum number instead of the standard deviation
5.  writability: subjective score 1-100 how easy was the code to write

All scores are then averaged for a final score.


The Languages
=============

1.  Python (implemented)
2.  Go
3.  Clojure
4.  Java
5.  C++
6.  C
7.  Haskell
8.  Erlang
9.  Node.js
10.  Ruby
