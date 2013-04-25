test: Setup/Files/1 Python/Result Java/Result
	cat Python/Result
	cat Java/Result

Python/Result:
	Python/Controller.py > Python/Result

Java/Result: Java/Controller.class
	java Java/Controller > Java/Result

Java/Controller.class: Java/Controller.java Java/Server.java Java/Client.java
	javac -g Java/Controller.java

Setup/Files/1:
	Setup/FileMaker.py

clean:
	rm Setup/Files/*
	rm Python/Result
