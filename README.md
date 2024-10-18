# retail-fake-data
I number of modules to generate fake data required for a typical retail business.  All the data is generated using the faker library in python.

Each module pertains to a single table and referential integrity is achieved through linking the tables with appropriate foreign keys in the App.py.

Arbitrary number of records for each table/file are defined in the App.py, update this as per requirements for more/less data.

Unless you need to add/remove fields, app.py is the only file that needs to be updated to customise number of records and foreign keys.

Sample data from an app.py run is available in the "data files" folder.
