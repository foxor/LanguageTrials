test: Setup/Files/1 Python/Result
	cat Python/Result

Python/Result:
	Python/Controller.py > Python/Result

Setup/Files/1:
	Setup/FileMaker.py

clean:
	rm Setup/Files/*
	rm Python/Result
