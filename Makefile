hello:
	echo "Hello from makefile"
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt