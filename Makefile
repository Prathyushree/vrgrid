.PHONY: setup test test-determinism test-partition lint run dash clean

setup:                       ## editable install so `python -m vrgrid.run` works
	pip install -e ".[dev]"

test:                        ## all unit tests -- must pass before any merge
	pytest -q

test-determinism:            ## same input twice -> identical map hash
	pytest -q -m determinism

test-partition:              ## 10^6 random points, exactly one cell per ring
	pytest -q -m partition

lint:
	ruff check .

run:
	python -m vrgrid.run --seq 08 --schedule 5/10/20/40

dash:
	python -m vrgrid.dash

clean:
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
	rm -rf .pytest_cache build *.egg-info
