# Example project

## Setup:
```sh
python -m venv .venv                # Create a python virtual environment
source .venv/bin/activate           # Activate it (This command will differ for Windows)
pip instal -r requirements.txt      # Install the dependencies
```

## Run:
```sh
python -m uvicorn app:app --reload
```

## Structure:
```
app.py                      # Main file
docs.py                     # Takes metadata from each route and compiles it for FastAPI
config.py                   # Environment variables, could use .env instead

Dockerfile

routes/
    L team.py
    L ctf/
        L start.py          # Separate file since it involves much more complex tasks
        L __init__.py       # Rest of the ctf routes go here
    L leaderboard.py
    L __init__.py           # Main router under `/api`, any misc routes go here
helpers/
tests/
```
