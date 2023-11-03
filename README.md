# CTF Backend example

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

To make the API routes clear without having to check each file, we organise the routes in separate python files.

Each file has their own router, eg. `/team`, with endpoints lying under it: `/team/list` `/team/login`

All individual routes (`/team/*`, `/ctf/*`) are then put behind `/api` in the `routes/__init__.py`, so we end up with `/api/team/*` and `/api/ctf*`.

In case a certain route has multiple complex tasks, they can be separated as a submodule. For example, the route `/api/ctf/start` will perform a lot of tasks (interacting with docker etc.), and hence has a separate file for it.

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
