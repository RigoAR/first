# Working on python 2.7

# Run program with no menu
run:
	python twenty_forty_eight.py

# Run program with menu visible
run menu:
	python twenty_forty_eight.py -menu="on"

# Run unit tests
test:
	python -m unittest test_board_class.py.py

# clean
clean:
	rm -f twenty_forty_eight.pyc

.PHONY: clean