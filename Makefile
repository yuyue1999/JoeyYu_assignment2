all: install format lint test

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black src --line-length 100 --verbose

lint:
	ruff check src/ --fix --verbose

test:
	python3 -m pytest -vv --nbval -cov=src -cov=lib test_*.py *.ipynb
	rm -rf *.png *.pdf


clean:
	rm -rf $(VENV)