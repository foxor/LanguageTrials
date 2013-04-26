test: Judging/Java Judging/Python Judging/Summary.py
	Judging/Summary.py

Judging/Python: Python/Result Judging/Score.py
	Judging/Score.py Python > Judging/Python

Judging/Java: Java/Result Judging/Score.py
	Judging/Score.py Java > Judging/Java

Python/Result: Python/Controller.py Python/Client.py Python/Server.py Setup/Files/1
	Python/Controller.py > Python/Result

Java/Result: Java/Controller.class
	java Java/Controller > Java/Result

Java/Controller.class: Java/Controller.java Java/Server.java Java/Client.java Setup/Files/1
	javac -g Java/Controller.java

Setup/Files/1: Setup/FileMaker.py
	Setup/FileMaker.py

clean:
	rm Setup/Files/*
	rm Python/Result
	rm Java/Result
	rm Judging/Python
	rm Judging/Java
