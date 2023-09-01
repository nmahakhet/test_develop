### Create env (Recommend python 3.8+)

$ python -m venv .venv

### Activate the virtual environment (on Windows)

myenv\Scripts\activate

### Activate the virtual environment (on macOS and Linux)

$ source myenv/bin/activate

### Install Lib

$ pip install -r requirements.txt

### Migrations database

Use `alembic` to migrations the database, example run `$ alembic upgrade head` for migrate database from alembic revision.

#### Running the migration

```
$ alebmic upgrade head
```

## Run app

` uvicorn app.main:app --reload`
