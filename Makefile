# Working on python 2.7

# Run 2048
run:
	python twenty_forty_eight.py

# Run unit tests
test:
	python -m unittest test_board_class.py.py

# clean
clean:
	rm -f twenty_forty_eight.pyc save.txt top_score.txt

.PHONY: clean