#!/bin/bash
poetry run flake8 src tests scrape_web.py
poetry run pylint src tests scrape_web.py
poetry run pydocstyle src tests scrape_web.py
poetry run bandit -c pyproject.toml -r .
poetry run pytest --cov --cov-report=html -n auto
# poetry run python scrape_web.py