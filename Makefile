.PHONY: run test clean

run:
	python3 main.py dummy_vfs

test:
	python3 -m unittest discover -s tests

clean:
	rm -rf __pycache__ src/__pycache__ tests/__pycache__ .pytest_cache