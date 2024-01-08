# Flask Practice

## Install

Install dependencies
```bash
poetry install
```

## Run in a local environment
(with poetry)

```bash
poetry run python wsgi.py
```
or
```bash
poetry run flask run --debug -h "0.0.0.0" -p 5555 --no-debugger --no-reload
```
