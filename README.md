# U.Group Data Engineering Challenge Answers
## J. Mark Daniels

### Instructions to Run Solution

1. Install Dependencies via Requirements folder (**build and populate requirements folder**)
2. Create cars.db by importing entirety of cars.csv into a sqlite3 database named 'cars.db'.
4. Run all cells of Jupyter Notebook ('DANIELS_data_engineering_answers.ipynb')
5. Run API Script ('cars_api.py')
6. Open following endpoints to access data:
    - http://127.0.0.1:5000/
    - http://127.0.0.1:5000/stores/
    - http://127.0.0.1:5000/vins/
    - http://127.0.0.1:5000/transactions/

### Components of the Solution

#### Database
The database is built using sqlite3. Opening the file in a text editor and in Numbers revealed some column mismatches and one row with faulty data cells. Once this was cleaned, the cleaned csv file was imported into a sqlite3 database table named Sales. From here, a jupyter notebook was employed to manipulate normalise the tables and conduct feature engineering using python and the pandas library. Once the database structure was set, the new tables were exported to cars.db via a dataframe to sqlite3 conversion.

#### API
The API was constructed in python using flask. Python comments were utilized to construct an outline of the endpoints needed to provide the functionality requested in the challenge document. CRUD functionality for particular data points is planned once a working API endpoint is confirmed.

### Challenges and Blockers
- MacOS Catalina update was causing issues in setting up virtual environments **SOLVED source activate ugroup_challenge**

- Balancing database normalization (star or snowflake modular construction) and ease of querying (one big database)

- Allow for scaling and evolution of database utilizing modular construction

- Many engine sizes are null **Possible Solution: cross reference with similar vehicles to populate LOWER PRIORITY**

- Minimize overhead by eliminating redundancy among tables

- Cannot import csv directly into sqlite due to table size mismatch **SOLVED**
    
    - Copied original database and imported into Numbers. Found and corrected error in row 22782. 

- Importing only one column at a time when using sqlite3 .import **SOLVED**

- Fact Table imports of foreign keys resulted in gross errors in data as well as Null/NaN values in ID columns.**SOLVED**
    
    - Tried recreating Fact Table in SQLite Studio as well as manually through terminal with same results.
    
    - Attempted to create Index on each, but could not import that into Fact Table either.
    
    - Used Studio to create autoincrement ID Columns in Dimension Tables **SOLVED**
    
    - Still won't import into Fact Table correctly
    
    ***Rebuilt all tables in Jupyter Notebook using Pandas and exported into sqlite3***

- SQLAlchemy part of cars_api isn't connecting to database correctly

- Reverted back to sqlite3 and basic Flask

### Attempted Features and Solutions
- Began utilizing SQLite Studio to make rapid modifications to database structure.

- Attempted to create decentralized star/snowflake structure. Decided to focus on getting something running first.

- Tried to use csv space stripper code from Stack Overflow to fix import problems.

- Deleted everything and restarted following tutorial in sqlite documentation.

- Create Fact table for individual transactions. Include: VIN ID, Store ID, PurchVal

- Create Dimension tables for Store_Num and VIN to create separate ID's that cascade any changes to Fact Table.

- Created Jupyter Notebook to quickly test changes and implement solutions.

- Creating Master Notebook for feature engineering in pandas with python. Will export resultant dataframes to sqlite. Just want to get something working quickly even if it is not pretty (ie perfectly balanced between ease of queries and normalization).

- Stepping through api creation tutorials to access database.

- Attempted various fixes for sqlaclchemy

- Tried using sqlite3 instead of sqlalchemy

### List of Dependencies
- python3
- jupyter notebook
- sqlite3
- pandas
- flask
- flask-restful
- flask-sqlalchemy
- flask-marshmallow
- marshmallow-sqlalchemy

## Areas for Improvement

1. Balance databae normalization and ease of query by snowflaking some tables to minimize overhead while preserving ease of use, scalability, and functionality.
2. Create aggregation features in pandas and export to database.
3. Incorporate aggregation features into API endpoints
4. Create additional filter features in the API:
    - Price
    - Inventory by Store Location
    - Average and median purchase prices per store
    - Metric capturing VIN churn (some VIN's were bought and sold more than once)
    - Sorted lists of most commonly sold vehicles (make and model) and vehicle types
    - Metric capturing profitability 
5. Create a script to automatically generate report of monthly sales by store.
6. Incorporate DateTime features into data collection efforts.
7. Create pipelines to automate the capture, cleaning, and processing of data into the database.
