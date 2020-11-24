# flask_sqlite
Simple Flask web application that demonstrates Flask-WTF and Flask-SQLAlchemy using a
SQLite database.

## Instructions
The scripts are written in Python3.
As always ensure you create a virtual environment for this application and install
the necessary libraries from the `requirements.txt` file.

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Start the development server

```
$ python run.py
```
Browse to http://0.0.0.0:8080

You can reset and reload the database by launching load_csv.py script, in the /app folder.

```
$ cd app
$ python load_csv.py
```


## About
I found this interesting repository: https://github.com/uwi-info3180/flask-sqlite.
I wrote a python script, "load\_csv.py", for loading csv data to the database.
I added two columns in the table, "uploaded\_by", in order to record the type of submission 
(by csv file or web form), and "request_timestamp", for logging requests.
In the "Add Measure" section, it is possible to insert temperature and duration fields only: 
the other fields, not supposed to be inserted manually, are automatically computed in the "views.py" script.
For the "Get Measures" section, I added a function in "views.py" and two html templates;
the request is logged in the "request_timestamp" field. Lastly, in the "Show Measures" section I inserted a table with the whole dataset.


