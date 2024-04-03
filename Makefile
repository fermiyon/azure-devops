hello:
	echo "Hello from makefile"
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C,E1120 main.py
test:
	python -m pytest -vv test_main.py