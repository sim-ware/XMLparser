# XMLparser
Parses XML info into a DB, returns sales rights information. Written in Python, making use of SQLite3 as a DataBase, and ElementTree for XML Parsing.

## To Run
First clone this repo, and 'cd' into the root directory.

Run the following command...
```
$ python app.py
```

...which will make use of the classes in the lib folder to Parse the XML Data. The XML Data is stored in the folder 'PerlegoXML'. Running the command creates a DataBase File, <b>'perlego.db'. To view its contents, from the root directory run:
```
$ sqlite3 perlego.db
```
This opens up a terminal interface to see the data. Available tables can be seen by running:
```
$ .tables
```
This should return the table <b>'bookSalesRights'. To see all its data, run:
```
$ SELECT * FROM bookSalesRights;
```
This will return all the data in the table for you to view in the console.
